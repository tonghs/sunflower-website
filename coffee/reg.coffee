def_view(
    'RegApp',
    'RegCtrl',
    ($scope) ->
        o = {}
        o.name = '1'
        o.startup_name= '2'
        o.phone= '3'
        o.email= '4'
        o.desc= '5'

        $scope.o = o

        $scope.submit =->
            $.postJSON '/j/reg', $scope.o, (o)->

)
