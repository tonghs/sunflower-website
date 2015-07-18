def_view(
    'LoginApp',
    'LoginCtrl',
    ($scope) ->
        o = {}
        o.user_name = ''
        o.password = ''

        $scope.o = o

        $scope.submit =->
            $.postJSON '/j/login', $scope.o, (o)->
                window.location.href = '/'
)
