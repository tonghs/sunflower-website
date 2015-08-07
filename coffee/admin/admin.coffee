
def_view(
    'LoginApp',
    'LoginCtrl',
    ($scope) ->
        o = {}
        o.user_name = ''
        o.password = ''

        $scope.o = o

        $scope.submit =->
            $.postJSON '/j/admin/login', $scope.o, (o)->
                if o.success
                    window.location.href = '/admin/index'
                else
                    $.alert_fail o.msg

)
