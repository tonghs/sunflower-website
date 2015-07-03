def_view(
    'RegApp',
    'RegCtrl',
    ($scope) ->
        o = {}
        o.name = 'test'
        o.sex = '1'
        o.age = 20
        o.blood = 'O'
        o.tall = 170
        o.weight = 120
        o.nation = '汉'
        o.birthday = '1987-10-06'
        o.marry = 0
        o.id = 123494994999499939
        o.phone= '189388477367'
        o.email= 'test@test.com'
        o.location = '北京市朝阳区西坝河北里201号院2号楼8单元502'

        o.startup_name= '2'
        o.desc= '5'

        $scope.o = o

        $scope.submit =->
            $.postJSON '/j/reg', $scope.o, (o)->
                window.location.href = '/reg_success'

)


$('#birthday').datetimepicker({
    format: 'yyyy-mm-dd'
})
