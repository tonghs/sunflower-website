def_view(
    'RegApp',
    'RegCtrl',
    ($scope) ->
        o = {}
        o.ico = 0
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
        o.exp = '工作经历'

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
            name: '仝华帅'
            title: 'CTO'
            desc: '描述描述描述'
            story: '话说当年盘古开天辟地之时（省略万字），有个荷兰小伙叫做李纳斯创造出了Linux,blabla…然后就有了tmux。'
        }, {
            name: 'LiLei'
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

        o.startup = {
            name: '天使汇'
            amount: 500
            stock: '10%'
            purpose: '团队建设'
            desc: '天使汇有什么好描述的'
            target: '创业者和投资人'
            point: '创业难啊'
            use: '去网站自己看，angelcrunch.com'
            advantage: '啥也不说了都在酒里'
            pattern: '赚钱，赚钱'
            sale: '营销模式'
            finance: '过亿了'
            risk: '没什么风险'
            plan: '没什么鬼话'
            equity: '没什么结构'
            sign: 1
        }

        o.about_me = {
            interest: '看书'
            idol: '不知道'
            dream: '吃饭不花钱'
            desc: 'NB到不行'
            motto: '还好还好'
            competition: '挑战杯'
            expectance: '请安啊'
            exp: '那是相当的惨啊'
        }

        $scope.percent = 0
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

$('#ico_up').uploader({
    uploading: (percent)->
        V().percent = percent
        V().$apply()
        if percent == 100
            percent = 0
    uploaded: (id, url)->
        V().o.ico = id
        V().$apply()
        $('#ico').css('background-image', "url(#{url}?imageView2/1/w/436/h/436)")
        
    error: (up, err, errTip)->
        console.log errTip
})
