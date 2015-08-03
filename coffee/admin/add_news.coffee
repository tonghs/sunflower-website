editor = new Simditor({
    upload:
        fileKey: 'file',
        url: 'http://up.qiniu.com/',
        params: {
            "token_url": "/j/upload_token"
        }

    textarea: $('#content')
    toolbar: [
      'title'
      'bold'
      'italic'
      'underline'
      'strikethrough'
      'color'
      'ol'             # ordered list
      'ul'             # unordered list
      'blockquote'
      'code'           # code block
      'table'
      'link'
      'image'
      'hr'             # horizontal ruler
      'indent'
      'outdent'
      'alignment'
    ]
    toolbarFloat: true
    toolbarFloatOffset: 50
    
})

window.def_news = (o)->
    if o.img
        $('#img-preview').css('background-image', "url(#{CONST.QINIU_HOST}/#{o.img}?imageView2/1/w/436/h/436)")
        $('#img-preview').addClass('preview')

    if o.content
        editor.setValue(o.content)

    def_view(
        'NewsApp',
        'NewsCtrl',
        ($scope) ->
            $scope.o = o
            $scope.percent = 0

            $scope.submit =->
                V().o.content = editor.getValue()
                V().$apply()
                $.postJSON '/j/admin/add_news', $scope.o, (o)->
                    $.alert_success '保存成功'
    )


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
