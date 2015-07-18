def_view(
    'LoginApp',
    'LoginCtrl',
    ($scope) ->
        o = {}
        o.name = ''
        o.user_name = ''
        o.password = ''

        $scope.o = o

        $scope.submit =->
            $.postJSON '/j/signup', $scope.o, (o)->
                $.alert_success('注册成功', ->
                    window.location.href = '/signin'
                )
)
