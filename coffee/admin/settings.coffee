window.def_settings_view = (o)->
    def_view(
        'SettingsApp',
        'SettingsCtrl',
        ($scope) ->
            $scope.o = o

            $scope.submit =->
                $.postJSON '/j/admin/settings', $scope.o, (o)->
                    $.alert_success '保存成功'

    )

