def_view(
    'RegApp',
    'RegCtrl',
    ($scope) ->
        o = {}
        o.name = 'test'
        o.sex = '1'
        o.age = 20
        o.blood = "#{CONST.ENUM.BLOOD.O}"
        o.tall = 170
        o.weight = 120
        o.nation = '汉'
        o.birthday = '1987-10-06'
        o.marry = 0
        o.id = 123494994999499939
        o.phone= '189388477367'
        o.email= 'test@test.com'
        o.location = '北京市朝阳区西坝河北里201号院2号楼8单元502'

        o.edu = [{
            start_date :  '1987-10-06'
            end_date :  '1987-10-06'
            school :  '燕山大学'
            major :  '电子信息工程'
            degree :  "#{CONST.ENUM.DEGREE.DIPLOMA}"
        }, {
            start_date :  '1987-10-06'
            end_date :  '1987-10-06'
            school :  '燕山大学'
            major :  '电子信息工程'
            degree :  "#{CONST.ENUM.DEGREE.DIPLOMA}"
        }]
        o.edu_ = {
            start_date: ''
            end_date: ''
            school: ''
            major: ''
            degree: "#{CONST.ENUM.DEGREE.DIPLOMA}"
        }

        o.team = [{
            name: 'test'
            title: 'CTO'
            desc: '描述描述描述'
            story: '话说当年盘古开天辟地之时（省略万字），有个荷兰小伙叫做李纳斯创造出了Linux,blabla…然后就有了tmux。'
        }, {
            name: 'test'
            title: 'CTO'
            desc: '描述描述描述'
            story: '前些天经朋友介绍认识了一个Linux利器，有了它，就能在Linux机器上为所欲为了，哦不，是更有效率的工作了。这个利器就是传说中的tmux，什么？没听说过，那且容我慢慢道来。'
        }]

        o.team_ = {
            name: ''
            title: ''
            desc: ''
            story: ''
        }

        $scope.o = o

        $scope.submit =->
            $.postJSON '/j/reg', $scope.o, (o)->
                window.location.href = '/reg_success'

        $scope.edu_add =->
            o.edu.push(jQuery.extend(true, {}, o.edu_))
            o.edu_ = {
                start_date: ''
                end_date: ''
                school: ''
                major: ''
                degree: "#{CONST.ENUM.DEGREE.DIPLOMA}"
            }

        $scope.team_add =->
            o.team.push(jQuery.extend(true, {}, o.team_))
            o.team_ = {
                name: ''
                title: ''
                desc: ''
                story: ''
            }
)


$('#birthday, #edu_start_date, #edu_end_date').datetimepicker({
    format: 'yyyy-mm-dd'
    autoclose: true
    language: 'zh-CN'
    minView: 2
})
