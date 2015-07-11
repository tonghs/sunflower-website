<%!
    from config import HOST
    from model import const
%>

window.CONST = window.CONST or {}

CONST.HOST = '${HOST}'
CONST.ENUM = CONST.ENUM or {}
CONST.ENUM.BLOOD = ${const.BLOOD.to_dict()}
CONST.ENUM.DEGREE = ${const.DEGREE.to_dict()}
