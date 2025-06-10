*作业一：用mlogit的方法研究婚姻目的的选择

*1、打开数据
use "E:\1year master\Stata17\作业\CGSS2021.dta"

foreach var of varlist A2 A3_1 A18 A4 A5 A69 A10 A8a A7a A15 B2 A43e {
	drop if `var'==. 
}
*2、变量处理

*因变量——结婚目的
recode B2(1=0 "情感目的")(2 4=1 "家庭目的")(3=2 "经济目的")(*=.),gen(purpose)
drop if purpose==.

*以下为解释变量
*性别
recode A2 (1=1 "male")(2=0 "female")(*=.),gen(gender)
*年龄
gen age=2021-A3_1
recode age (18/34=0 "young")(35/64=1 "mid")(65/95=2 "old")(*=.),gen(agegrp)
*城乡
recode A18 (1=0 "rural")(2 3 4 5=1 "urban")(*=.),gen(region)
drop if region==.
*民族
recode A4 (1=1 "han")(*=0 "minority"),gen(ethnic)
*宗教信仰
recode A5 (1=1 "noreligion")(*=0 "yesreligion"),gen(religion)
*婚姻
recode A69 (1 2=0 "未婚")(3 4=1 "已婚")(*=2 "离异或丧偶"),gen(marriagenew)
*政治面貌
recode A10 (4=1 "party")(*=0 "other"),gen(party)
*收入
drop if A8a>=9999996 & A8a<=9999999
gen wage=ln(A8a+1)
*教育
gen edu=.
replace edu=0 if A7a==1
replace edu=6 if A7a==2 | A7a==3
replace edu=9 if A7a==4
replace edu=12 if A7a==5|A7a==6|A7a==7|A7a==8
replace edu=15 if A7a==9|A7a==10
replace edu=16 if A7a==11|A7a==12
replace edu=19 if A7a==13
replace edu=. if A7a==.
recode edu (0 6 9=0 "初中及以下")(12 15=1 "高中及大专")(16 19=2 "大学及以上")(*=.),gen(edunew)
*健康状况
recode A15 (4 5=1 "healthy")(*=0 "unhealthy"),gen(health)
*地区(按去年人均gdp排名 0为不经济发展较次 1为发展较好)
gen area=.
replace area=0 if provinces=="辽宁省" | provinces=="山西省" | provinces=="宁夏回族自治区" | provinces=="河南省" | provinces=="河北省" | provinces=="广西壮族自治区" | provinces=="甘肃省" | provinces=="湖南省" | provinces=="江西省" | provinces=="安徽省" | provinces=="陕西省" 
replace area=1 if provinces=="北京市" | provinces=="江苏省" | provinces=="福建省" | provinces=="浙江省" | provinces=="重庆市" | provinces=="湖北省" |provinces=="内蒙古自治区" | provinces=="山东省" 
*社会层次
recode A43e (1 2=2 "中上层")(3 4=1 "中下层")(5=0 "下层")(*=.),gen(level)
drop if level==.

*3、描述统计
fre purpose gender agegrp region ethnic religion marriagenew party edunew health area level
sum age wage edu

*4、推断性分析
tab purpose gender,column chi2
tab purpose agegrp,column chi2
tab purpose edunew,column chi2

*5、回归模型
*多分类logit/mlogit
mlogit purpose gender age region ethnic religion marriagenew party wage edu health area level,base(1) nolog //以家庭目的为基准
mlogit purpose gender age region ethnic religion marriagenew party wage edu health area level,base(0) nolog //以情感目的为基准

*6、正式表格输出
eststo clear
quietly mlogit purpose gender age region ethnic religion marriagenew party wage edu health area level,base(1) nolog
eststo m1
quietly mlogit purpose gender age region ethnic religion marriagenew party wage edu health area level,base(0) nolog
eststo m2
esttab,compress se r2 mtitle star(* 0.1 ** 0.05 *** 0.01)
esttab m1 m2 using mlogitness.doc, se r2 replace compress //以word的形式保存



*作业二：用调节效应的方法研究性别观念

*1、打开数据
use "E:\1year master\Stata17\作业\CGSS2021.dta"

foreach var of varlist A2 A3_1 A18 A4 A5 A69 A10 A8a A7a A15 {
	drop if `var'==. 
}

*2、变量处理
*因变量——性别观念（连续变量）
recode A42_1(1=1)(2=2)(3=3)(4=4)(5=5)(*=.),gen(A421)
recode A42_2(1=1)(2=2)(3=3)(4=4)(5=5)(*=.),gen(A422)
recode A42_3(1=1)(2=2)(3=3)(4=4)(5=5)(*=.),gen(A423)
recode A42_4(1=1)(2=2)(3=3)(4=4)(5=5)(*=.),gen(A424)
recode A42_5(1=5)(2=4)(3=3)(4=2)(5=1)(*=.),gen(A425) //反向赋值
drop if A421==. | A422==. | A423==. | A424==. | A425==.
gen attitude=A421+A422+A423+A424+A425

*解释变量
*性别
recode A2 (1=1 "male")(2=0 "female")(*=.),gen(gender)
*年龄
gen age=2021-A3_1
gen ages=age*age
*城乡
recode A18 (1=0 "rural")(2 3 4 5=1 "urban")(*=.),gen(region)
drop if region==.
*民族
recode A4 (1=1 "han")(*=0 "minority"),gen(ethnic)
*宗教信仰
recode A5 (1=1 "noreligion")(*=0 "yesreligion"),gen(religion)
*婚姻
recode A69 (1 2 6 5 7=0 "unmarried")(3 4 =1 "married"),gen(marriage)
*政治面貌
recode A10 (4=1 "party")(*=0 "other"),gen(party)
*收入
drop if A8a>=9999996 & A8a<=9999999
gen wage=ln(A8a+1)
*教育
gen edu=.
replace edu=0 if A7a==1
replace edu=6 if A7a==2 | A7a==3
replace edu=9 if A7a==4
replace edu=12 if A7a==5|A7a==6|A7a==7|A7a==8
replace edu=15 if A7a==9|A7a==10
replace edu=16 if A7a==11|A7a==12
replace edu=19 if A7a==13
replace edu=. if A7a==.
recode edu (0 6 9=0 "初中及以下")(12 15=1 "高中及大专")(16 19=2 "大学及以上")(*=.),gen(edunew)
*健康状况
recode A15 (4 5=1 "healthy")(*=0 "unhealthy"),gen(health)
*地区(按去年人均gdp排名 0为不经济发展较次 1为发展较好)
gen area=.
replace area=0 if provinces=="辽宁省" | provinces=="山西省" | provinces=="宁夏回族自治区" | provinces=="河南省" | provinces=="河北省" | provinces=="广西壮族自治区" | provinces=="甘肃省" | provinces=="湖南省" | provinces=="江西省" | provinces=="安徽省" | provinces=="陕西省" 
replace area=1 if provinces=="北京市" | provinces=="江苏省" | provinces=="福建省" | provinces=="浙江省" | provinces=="重庆市" | provinces=="湖北省" |provinces=="内蒙古自治区" | provinces=="山东省" 

*3、描述性与推断性统计
fre gender region ethnic religion marriage party health area
sum  attitude age wage edu
ttest attitude,by(gender)
bysort edunew:sum attitude
anova attitude edunew

*4、回归分析
regress attitude edu gender age ages region ethnic religion marriage party wage health area,robust //模型一

regress attitude c.edu##gender age ages region ethnic religion marriage party wage health area,robust //模型二
quietly: margins gender,at(edu=(0(2)20))
marginsplot, noci

*输出表格
eststo clear
quietly regress attitude edu gender age ages region ethnic religion marriage party wage health area,robust
eststo m1
quietly regress attitude c.edu##gender age ages region ethnic religion marriage party wage health area,robust
eststo m2
esttab,compress se r2 mtitle star(* 0.1 ** 0.05 *** 0.01)
esttab m1 m2 using jiaohuxiaoying.doc, se r2 replace compress //以word的形式保存