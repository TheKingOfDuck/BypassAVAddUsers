<?php
header("Content-Type: text/html;charset=utf-8");
?>
<html>
<body>
<table border="1" width="300">
  <tr>
    <td width="100">文件大小</td>
    <td width="200"><div id="filesize">未知长度</div></td>
  </tr>
  <tr>
    <td>已经下载</td>
    <td><div id="downloaded">0</div></td>
  </tr>
  <tr>
    <td>完成进度</td>
    <td><div id="progressbar" style="float:left;width:1px;text-align:center;color:#FFFFFF;background-color:#0066CC"></div>
      <div id="progressText" style=" float:left">0%</div></td>
  </tr>

<script type="text/JavaScript">
//文件长度
var filesize=0;
function $(obj) {return document.getElementById(obj);}

//设置文件长度
function setFileSize(fsize) {
    filesize=fsize;
    $("filesize").innerHTML=fsize;
}

//设置已经下载的,并计算百分比
function setDownloaded(fsize) {
    $("downloaded").innerHTML=fsize;
    if(filesize>0) {
        var percent=Math.round(fsize*100/filesize);
        $("progressbar").style.width=(percent+"%");
        if(percent>0) {
            $("progressbar").innerHTML=percent+"%";
            $("progressText").innerHTML="";
        } else {
            $("progressText").innerHTML=percent+"%";
        }
    }
}
</script>
<?php
error_reporting(0);
ob_start();
@set_time_limit(300);
$url="http://www.gzdata.net.cn/tmp/python-3.7.2.post1-embed-win32.zip";
$newfname="py.zip";
$file = fopen ($url, "rb");
if ($file) {
    $filesize = -1;
    $headers = get_headers($url, 1);
    if ((!array_key_exists("Content-Length", $headers))) $filesize=0;
    $filesize = $headers["Content-Length"];
    if ($filesize != -1) {
        echo "<script>setFileSize($filesize);</script>";
    }
    $newf = fopen ($newfname, "wb");
    $downlen=0;
    if ($newf) {
        while(!feof($file)) {
            $data=fread($file, 1024 * 8 );
            $downlen+=strlen($data);
            fwrite($newf, $data, 1024 * 8 );
            echo "<script>setDownloaded($downlen);</script>";
            ob_flush();
            flush();
        }
    }
    if ($file) {
        fclose($file);
    }
    if ($newf) {
        fclose($newf);
    }
}

class Unzip{
    public function __construct(){
        @header('Content-Type: application/zip');
    }
    
    public function unzip($src_file, $dest_dir=false, $create_zip_name_dir=true, $overwrite=true){
        if ($zip = zip_open($src_file)){
            if ($zip){
                $splitter = ($create_zip_name_dir === true) ? "." : "/";
                if($dest_dir === false){
                    $dest_dir = substr($src_file, 0, strrpos($src_file, $splitter))."/";
                }
                $this->create_dirs($dest_dir);
                while ($zip_entry = zip_read($zip)){
                    $pos_last_slash = strrpos(zip_entry_name($zip_entry), "/");
                    if ($pos_last_slash !== false){
                        $this->create_dirs($dest_dir.substr(zip_entry_name($zip_entry), 0, $pos_last_slash+1));
                    }
                    if (zip_entry_open($zip,$zip_entry,"r")){
                        $file_name = $dest_dir.zip_entry_name($zip_entry);
                        if ($overwrite === true || $overwrite === false && !is_file($file_name)){
                            $fstream = zip_entry_read($zip_entry, zip_entry_filesize($zip_entry));
                            @file_put_contents($file_name, $fstream);
                            chmod($file_name, 0777);
                            
                        }
                        zip_entry_close($zip_entry);
                    }
                }
                zip_close($zip);
            }
        }else{
            return false;
        }
        return true;
    }
    public function create_dirs($path){
        if (!is_dir($path)){
            $directory_path = "./";
            $directories = explode("/",$path);
            array_pop($directories);
            foreach($directories as $directory){
                $directory_path .= $directory."/";
                if (!is_dir($directory_path)){
                    mkdir($directory_path);
                    chmod($directory_path, 0777);
                }
            }
        }
    }
}

$z = new Unzip();
if($z->unzip("py.zip",'./py/', true, false)){
    echo <<< EOT


  <tr>
    <td width="100">解压进度</td>
    <td width="200">Done</td>
  </tr>

EOT;
}

if(unlink("./py.zip")){
    echo <<< EOT

  <tr>
    <td width="100">清理进度</td>
    <td width="200">Done</td>
  </tr>
</table>
EOT;
}
?>
</body>
</html>
