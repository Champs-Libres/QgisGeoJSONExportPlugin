<?php 
error_reporting(0);

function updload() {
    $input_field_name = 'uploaded_file';
        $destination_path = '../data';
    if($_POST['destination_path']) {
        $destination_path =  $_POST['destination_path'];
    }
    if (is_uploaded_file($_FILES[$input_field_name]['tmp_name'])) {
        $file_name = $_FILES[$input_field_name]['name'];
        $file_extension = pathinfo($file_name, PATHINFO_EXTENSION);
        if($file_extension === 'geojson' or $file_extension === 'json') {
            $file_destination = $destination_path . "/" . $file_name;
            if (move_uploaded_file($_FILES[$input_field_name]['tmp_name'], $file_destination)) {
                echo '{"code": 1, "message": "file uploaded"}';
            }
            else {
                echo '{"code": -1, "message": "can not move the file to '.$file_destination.'"}';
            }
        } else {
            echo '{"code": -2, "message": "only json or geosjon files accepted"}';
        }
    } else {
        echo '{"code": -3, "message": "no uploaded_file"}';
    }
}

updload();

/*
<form enctype="multipart/form-data" method="post">
    <inpyt type="text" name="destination_path">
    <input type="file" name="uploaded_file">
</form>
*/