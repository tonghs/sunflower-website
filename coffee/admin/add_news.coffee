def_view(
    'NewsApp',
    'NewsCtrl',
    ($scope) ->
        o =
            title : ''
            content : ''

        $scope.o = o

        $scope.submit =->
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
