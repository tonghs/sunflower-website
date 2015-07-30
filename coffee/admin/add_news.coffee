def_view(
    'NewsApp',
    'NewsCtrl',
    ($scope) ->
        o =
            title : ''
            summary: ''
            img: ''
            content : ''

        $scope.o = o
        $scope.percent = 0

        $scope.submit =->
            V().o.content = $('#content').val()
            V().$apply()
            $.postJSON '/j/admin/add_news', $scope.o, (o)->
                $.alert_success '保存成功'
)

editor = new Simditor({
    upload:
        fileKey: 'file',
        url: 'http://up.qiniu.com/',
        params: {
            "token": "/j/upload_token"
        }
    textarea: $('#content')
})


$('#img_up').uploader({
    uploading: (percent)->
        V().percent = percent
        V().$apply()
        if percent == 100
            percent = 0
    uploaded: (id, url)->
        V().o.img = id
        V().$apply()
        $('#img-preview').css('background-image', "url(#{url}?imageView2/1/w/436/h/436)")
        $('#img-preview').addClass('preview')
        
    error: (up, err, errTip)->
        console.log errTip
})
