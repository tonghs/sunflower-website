window.def_settings_view = (o)->
    def_view(
        'SettingsApp',
        'SettingsCtrl',
        ($scope) ->
            $scope.o = o

            $scope.submit =->
                $.postJSON '', $scope.o, (o)->
                    window.location.href = '/reg_success'

    )

