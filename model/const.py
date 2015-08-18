#!/usr/bin/env python
#coding: utf-8

from enum import IntEnum

class IntEnum_(IntEnum):
    @classmethod
    def to_dict(cls):
        d = dict()
        for o in cls:
            d.update({o.name:o.value})

        return d


class BLOOD(IntEnum_):
    O = 10
    A = 20
    B = 30
    AB = 40

BLOOD_CN = { 
    BLOOD.O.value:'O',
    BLOOD.A.value:'A',
    BLOOD.B.value:'B',
    BLOOD.AB.value:'AB'
}


class DEGREE(IntEnum_):
    DIPLOMA = 10
    BACHELOR = 20
    MASTER = 30
    PHD = 40

DEGREE_CN = { 
    DEGREE.DIPLOMA.value:'专科',
    DEGREE.BACHELOR.value:'本科',
    DEGREE.MASTER.value:'硕士',
    DEGREE.PHD.value:'博士'
}


class NEWS_CATAGORY(IntEnum_):
    STARTUP = 0
    NEWS = 1

NEWS_CATAGORY_CN = {
    NEWS_CATAGORY.STARTUP: '路演项目',
    NEWS_CATAGORY.NEWS: '大事记',
}


if __name__ == "__main__":
    pass
    print BLOOD.to_dict()

