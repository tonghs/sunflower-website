
def_view(
    'LoginApp',
    'LoginCtrl',
    ($scope) ->
        o = {}
        o.user_name = 'tonghs'
        o.password = 'tonghs'

        $scope.o = o

        $scope.submit =->
            $.postJSON '/j/admin/login', $scope.o, (o)->
                if o.success
                    window.location.href = '/admin/index'
                else
                    alert o.msg

)
