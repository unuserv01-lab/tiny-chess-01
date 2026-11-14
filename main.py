# tiny-chess-01 entry v2 (see README.md for the v1 diagnosis and changes)
import json,os,time,urllib.request as r
U=os.environ["MAKEFUN_ENV_URL"]
V=[0,100,320,330,500,900,0]
Y=b"KKKK}}}}UU_iPPUdKKK_PFAKPUU7KKKK##--#7KK-KUZ-PZ_-KZ_-PUZ#7KP##--7AAAAKKKAKPUAPPUAKUUAUUUAPKK7AAAKKKKPUUUFKKKFKKKFKKKFKKKFKKKKKKP7AAFAKKKAKPPFKPPKKPPAPPPAKPK7AAF7AAFAKKKAKPPFKPPKKPPAPPPAUUU_iUK"
J=[14,18,31,33,-14,-18,-31,-33]
D=[1,16,-1,-16]
E=[15,17,-15,-17]
G="abcdefgh"
O=(0,0,J,E,D,D+E,D+E)
S={0:2,7:1,112:8,119:4}
F=100000
Z=60000
B=[0]*128;T=1;C=0;W=-1;K=[4,116];A=[];N=0;R={};L=[0]*128;P=[]
X=Exception
exec(__import__('lzma').decompress(__import__('base64').b85decode(b'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;1i1oyIlY>8A$(5*+@BAFs^2^^@T<va-$D21VgR2hEie#+F(qi$2h_s16Qq93G!$h=xEs+{k<-r67-$DMRaFLN!@;)(DufD*wBF;215wM+{y+A)=<bQ+6p$j?PN#wLX<{@%bpUMKT0%9PETtdx@8?od*c{_*~4U~sn|Z*XXDgE3tg7q3-lOj#vYoW;t0}8Jb7q>`_W7<sk(+UHy1Lfe$2c>jAwY&QBI>R+b5fhiAz<8vuY`L_{j}^v@Q<5A5ve(MOY?HdH8*!K0cZ=W5>5nB>ag#pLspfFQ2hw_mdP%|K2G7rz{Eno5b8j4?`Wm4P_6fNsLqsX@W9ruuU!a5W)8dQ%mR{sdc<!n2|3^?nW70CTCMWGS*uS%ZIPBSqv3#UyjdC47RcMAc_O3@RLu8pXbCkd+}Hp$YjI&r2)r*VG|!2>5?6XLu|qo7{JdB=A}{DT1sP}^!zeE2j8aP9wdF)B!^{Jjz6osa}*M=q7C`h7VEcxt?!6InV7f;MC`B<I+N=`TN)zRnJm2Q>8>@-WJ(piZcUlC&F>kjaxIJ$53Rqhy5GW4el|>?t5EbYn^L~Y8xI~Fb}k=a94oNI_X8~ziVYmB&QXeAiAtmqUO&(m8n(vqp}gkAQV}y@H{x}_&{6G_yTngvQ+Nl0o4L+4CJYgA9fGy5NQ|yPbQM~QxIm=gsV12jR#LX$MFyIhF9l&aXx>E^U?EjReKy>+FjpgXv;bjGapoJ`HLlV3D+wz4+jf_SX3ztAYJ#BZE;MP^G~<gGLi(^{lv<Kd+e5(Z9U&1=+nxS%4B#+AQlRbEwW}u80)czICi3*$P~r@xJMv|1ZE(=MjKID1Phq;LpnEc*u}P4dM6q|LiBnALw{euN+0G?NUcxv)1U_TIR3jR$@M=zo-P#<)8X1qsb-64iQ<5My@F|avKp{^X{x1@2(@dR5BE5n3)_oVli@LCpygAS)=on^Hz^bTnWZ{_<Zwc|5{;>;Tq@D5XTGvW}Y=NTi<+-(qtx<Q13bg9tSo4rPWVc;tXmEP;1CZtD(LK8*!t`uuv~F*sTpGCf!u^XBy)t-AIhj5K1wm*Rc%KSU*(zp{JZJC!eD)ePP=l96J08fQlSY|@xLgzn{v}sg%iRQwaY%`2?d2mx=zY5^l%Dn>dZXR{YMwcTeg=1U8=12hpDslQe&y#^6dh9E)w?|as~6Sq$W!DB{rWMB#+c7w)6G7wWIaf&#xd2SBLD@n|LL6z-4wBYVx_@)xW8xm#1I$b(53nLt~b1@qaWsGhQGHmit3a%?>m~86F3n)b`}9KTAcg*mLRg&5zr6ts2c4|;a}OlsN%#(mT(HlzC3Jloj@uP#}A+!^hh|xD_QevG3G^@HkyOjF~vbPiWm`Ok0J@1@kL;?!s&SZG0Dvku3lZbWp8{-7!bV^!4Wdz-arMSxChedU7EqsS4%XYbHhbvz${W05*8ZdloHflG#*{zcuQ?mh)pjM#5?oU&suk0%m~phnKWPMutMu@-#9aT7H!-WK5dRz;G5R4x2JKyAGEQgne9U>hU{5(KA0Ao(yTEwNNZjp*GPOIRb@nB_WCCqD9uHLZCMLyz?~x=jdI6VVLp;aHwRm!aPZu|W_8bdvP+v!f~IK`CO%<>LavZ1V?|%2{&A&ADp-^H<iE|j-|&Iu6Iiz=h<a1({o5OgJ8+D%{agp@LjrQafj4<pcUW=w4^Hm)`&lyJACZ+L0PA;J1W6``B+0ylUkVNS>qyj7t}GBMac_b~69Z_!pC&6i?vRzHI&dDTW9G-IwF1RTOv-}{1J(W|N<G|Yq~M8|u}VY%G_tvZ>>6;+KCw-y(3J*#VytOSrZe3$i|3$Y%Dh<+Qh75K4Uz*ev}k342Qba6vh)Sm;tjV}P|D#9J135PZAdZh)b7qRHiSX1owLjGzm^%AzeifP?3a}y3RG@;M}#gjP!`~t3HkQCU^9|p@mE_}l*-E4Dwq)a==Vk2EXgXuOwhCBPOP+~^NJhsxB=|}?fwpSHfrD<bvM(L_h)4iFTmT-#+i0pMN=iKvoj6gOg@wDW#aJke$s<{o*)B$r|Nd8(81{U7&#Z<7Ax2AMiW`)q&Z4B4bxDZi11|#M2vrLlL))1TjiNMChkxg%KfMO3CvbpE}8&qZ!mFE4*@rk6h`lLP*zilk|tiu<J=uH@WxY59eY9KHPx|xtD5ghHl+)busTE)Wnbz&L)el_UnbX9pw@?<wE)03g%&U3P)f0>^XS|8Bk!6d%L6^Qj1@iO(pj_sM1Z^z{ag8Y50T2P^8w-5H1nsjf5Ub_NymZ1L}r{+p$>N)dJv+;@rYEj-J--cM=X64twiae_O*wD6%r5Sk=E9OGU32zV)B~%7DZsm{Qdo9_z-6!0Ah3<n5{l8TM{>?tRHvgr1|L&6IWy+t<`MnPXyyD??j>KWYsgZ86mrx0eutg{EUZ}wxvF{!JpFDt#iT|u%)Cki}-=~yA}pO@3W$#uipr@)^z=UH2b(}VY_=VDw`DJ9+i^n5d$}5!Pin~j+7vBqK(Lm`=Kn`2&vsrZ3f!c;vSILsaidG_JfN{9{~w1rM9%OhJ%jDCqJzI+0oX|b4oRy<ss$6?QtzFf78~{SO1PMXfEsbm@8w~?N?{AtCLqCdg*|72vvd|b6RJ;D{pU^osG!`)GHjuV52i??ZdEw`T^+~rTbmQ7k?rzo{{zK6JM+9Pa^wD2=KG<@Yg}!clOfiZj*UhI(u?cu>q(;7yH=l!Yl#OF5_QLX}L7#3F}xZ{k$O6rQPgr459R3Gp+nc>s5_%fyiVRyAZy5EP&*dj6%2NB7D6y1?)bX-P#Ye1qD8R<G2>JyXFBfhh`Y8eRKZAfv_dNd|Zf3mPZ8f@Bjb+-M&(yp?)s<00Gw#j3)p9o*!civBYQl0ssI200dcD')).decode())
while 1:
 q=o("/game",{})
 if q["status"]=="done":break
 while q["status"]=="your_move":q=o("/move",{"game":q["game"],"move":n(q["fen"],q["legal_moves"])})
# end of main.py
