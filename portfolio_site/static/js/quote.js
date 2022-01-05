$('#pType').change(function(){
    $sel = this.value;

    if($sel==1){
        $('#web_development_form').css('display', 'block')
    }else{
        console.log($sel)
    }

})

// Web dev form
$('#web_dev_info').change(function(){
    $('.web_info').css('display', 'block')
})

