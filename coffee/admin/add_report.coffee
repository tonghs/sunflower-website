window.def_report= (o)->
    if o.img
        $('#img-preview').css('background-image', "url(#{CONST.QINIU_HOST}/#{o.img}?imageView2/1/w/436/h/436)")
        $('#img-preview').addClass('preview')


    def_view(
        'ReportApp',
        'ReportCtrl',
        ($scope) ->
            $scope.o = o
            $scope.percent = 0

            $scope.submit =->
                $.postJSON '/j/admin/add_report', $scope.o, (o)->
                    $.alert_success '保存成功', ->
                        location.href = '/admin/reports'

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
