# 20000 20000 바이트 챌린지
import zlib,base64;from itertools import product;import sys
sys.setrecursionlimit(100000)
dd=lambda x:zlib.decompress(base64.b85decode(x)).decode("utf-8")
def G(x,y,f,di):
  dx,dy=f[di]
  for i in range(1,5):c[y+dy*i][x+dx*i]="!"
def ib(x,y):return 0<=x<1025 and 0<=y<1025
D,i=[chr(ord("A")+i)for i in range(26)]+[chr(ord("a")+i)for i in range(26)]+[chr(ord("0")+i)for i in range(10)]+["+","/"],int(input());D2={v:i for i,v in enumerate(D)}
if i==0:print("BOJ 20000")
if i==1:print(*['#include <cstdio>\nint main(){\n    int N;\n    scanf("%d",&N);']+[f'    {"else "if i-1 else""}if(N=={i}){{\n        puts("{i*4}");\n    }}'for i in range(1, 20001)]+['    else{\n        puts("Still working on it...");\n    }\n    return 0;\n}'],sep="\n")
if i==2:
  s,a,b="BaekjoonOnlineJudge!",["B"],["B"]
  for i in range(1,20):a+=[s[i]]+b;b=a[:]
  print(*a,sep="")
if i==3:
  a="01000001101101110001110001011001000011000111110001011010100010101110111100101001000110001110001000011011111001000010101011100011010100011000010101101100000011100000110011101111011001010011000110110111001110111001111000101011001111010111010110001000101010100101000110001001110101110110111100010001011110011110001110011011100010111011110101010101111100011100101001110101111101100110010111110110011010011001111110001110101110010100110100000100000100010000000000000000000000000000000000000000000000000000000000000000011110100101111100000011101001010111001011001111001010111011010111110000011000010001001111011110111101100111000111011101010000110100001100100110011000110100110110000101101001001011100111101010010110111010110101111111111111111101000100101001100011001000000111101100001000000100101000011101100100101101111011001101101111010010011010000010111001100010000100100011101011100100101000010110100011001000011111001010110100011110110111000010100101100100111100101000100011001011101001011001110100000101101011000011010111011101001101110010010101100001010101111100110111111110010110101011011000101111111101101111001000100100001110011011110111110111001011111111111111111111111111111111111111111111111111111111111111111011010001001011101100011101001010100101110101100010100110000011010011100001010101110000011011011010111000101000110010101001011111100010011001000111100001011101101011100110000111010110001001001011001101000000111010111010101010000100101011001101111011011110101101011000011000000000010000010110100111111101000111100010000011000001000101010111100000111000111101101011101100100100111111011101011101001010101100001001101000001001100101011101000000110100101110100011010110100110011011100101111000100001011001010110110101101110011101111100001001010110111010010101111100100111110010000010111110010000011101101001011010110011111101111000001101000111111000101111011111011111010111001001101101011010110000010101101101100010000100101111001110000010010011110011111001101011111100001101000111110111000011100111100001000101011110111011110000000001";b,c=[[0]*2**(i+1)for i in range(10)]+[[int(v)for v in a]],[[" "]*(1025+i)for i in range(1024)]
  for i in range(9,-1,-1):
    for j in range(2**(i+1)):b[i][j]=b[i+1][2*j]|b[i+1][2*j+1]
  for i in range(11):
    for j in range(2**(i+1)):
      if b[i][j]==0:continue
      x,y,z = 1024*(2*(j//2)+1)//(2**i)-1,1024-(2**(10-i)),"/"
      if j&1:x,z=x+1,"\\"
      for _ in range(max(2**(9-i),1)):
        c[y][x]=z;x,y=(x+1 if j&1 else x-1),y+1
  for v in c:print(*v, sep="")
if i==4:
  s,p,k=[["#"]*(j+1)for j in range(1000)],[0]*1025,1024;p[:2]=[1,1]
  for x in range(1,int(k**0.5)+1):
    if not p[x]:p[2*x:k+1:x]=[1]*(k//x-1)
  for i in range(1000):
    for j in range(i+1):
      s[i][j]="."if p[i^j]else"#"
  print("\n".join(["".join(i)for i in s]))
if i==5:print(dd(b'c$^iNHMZq25JVT`z)YdxnVId(%*<Z>{0Wrm^y!l7RtefSqU{*^w;(VjTN&jJ!IEzc>*r8aopgz+l@-~lt$G-v#EfJV>0bq_3oid=RjJJR1y`To`4WdPAw$@5&fbIIAfF!4U+D^_RBo$F0XQk3VcEs4!^KUq_Ce>yp36;5220OchEi)dSpCw=Fa#l(RPLpjaMO3`Fd81U2sgToV*Ws<Ir&D^OuUzyB~3b{E<o)Cu8M)drS?OUeZ})2P~)o7Oz0}9F7>fW<443sDbaZ@o}_4(r+>E!u;@13=`!saS@xwX<0AEP_c84U4-+sHiYbbmf!&NBiWq>-^ug!}9V1D8{hNFG;Xa!_z(bZvpuQHv1RaVc*)<Pf1qEMkCkR#186O`m8AYm5mVr6+Gm_CAGu_uKP>YuO{RlqoW5wU`wcG0hh#7kG7tx)qvH&?PU|@2eb64sdY-RVB?cbLTj+&%_#Fi_>X*XdYH;FMTv#e5`59eR$QFS8^i+x)I0FxPQ@3mto9|3;MibPE<(6JKPc_agLzH~v=M=TLlxwAUD*G6lg<c+rux1S9zZ*p4&@Oc`C{6cPY{#X(m?upwvru%!rG2n7ydh+bBTrw=FFvNbqui=ZM=<Ax{+RVvO2FQ8?XQCfzAG0Z(IAlqrXD;q-D=p6@G-fKAFsfs+<a|TJ99wk*CLswmsbZNLGY`KOCE9&FC&TnKb|r9|_w2q<eIZgA@!|8dHtjvd@`wXC%ul`}?Kq$$5s9LG*so$9B@yOt&h-0`P)XoSB3HVhYHnm-*?V79<(hHm%*?o49D3JEWxBNYu5HjDZrZWscr<AW?k4<-8abch6${VIe^1y+{o!I3{!TLgj{0#}CcLoA2qW{Yz~)x34C7@HI@IlRf0cXW=uIx$r9+p{)6HTik(sk@@fOXico@+<%%^`j=lihrfWKZt#Uhl4)JP?gaHnh%QgTkwFy%=9gDwf~)x+}GwmXN1J#VFkQv-~m&_H;(t2dnX+MLD>fl$W}y1}PLlAr<<F&4WvfHh#;LVPc!m<-ePUh>A^l;{HyTLbAdmTJ`deh@t$v4BrQK9bIzDWavEBRR&B{^bfoNWV9Gpu#`InTT675pv_b^q$|-3*>Y-Yl-NR`iUzW#!;yhv-fHQi*as8XHK028;U;Zy27a-0!^>fd+M`0Rv%F4Xy|+(X}q$Qh&$dv?Fx^^Q=vU*^mPx*97T?+fi!I~YZzb|G3OI3<sJ(;J;6;WEn}dKR<Ws)+~5G<MqX{j6j>Fke0M})+gEyA$Kp81WBWTMeqYbwc)akTPo29)O&i5Q`BMHKjjL0QWk9FoJI?sAS&^SlES4qsz-CrByrTkt3Ya+YdiLFCbq(UEal~;C4t86_%*jC{UQ%-cr(`aO_qshFwv^6EHW11F`Z0@7SRgrwpnDr>x2ayr8OTVVXx!)ME4Sp;LCS~lOK!hpT~-8%!%#ABNg>x|k$*u`aiK4moj;2Ni~<kOKUJ=51#l};t)oD=aM3U4U2p6UH=pB)>-54mNPRCWIK>Kw0}W@3Wk?9p{58JW7M`Soie*6T)kg*}(&>|`NXO2}+sbrEdzja<DB-SPc>7bqC_0FVd*ZB0ZrX@fz5YbD?DH@s%>2}-8M4LrqCYvEIx~E1b4*xeSrM}=Jz9K$fiy!kV3%&M9*n7jMo~k`xi>ny7ruWN7cX$sfz|nkjf|kxr4GKj_8p2za#RUgUY6m@P<*^x4aztG=69Ncmn~W+=G~r%3?lZ@hEmO3(5!~}L_m`fNbJ(o<4l+a1J6<yC09@GA**=0PHCB`ESBs=KfR-WK!r&%#>qzysc}-;?HTD0$<(2*RE}<Akil(k`plrW?5wUM=`uiJ8%kYF8@rFRd8q6o6i^l>0Y9%+2lC4QIC0G41M4x1*&Bh#^{M0CaRVv;g(VaGoh9TmJhK>Wbrs(=eoa&j;ag82NUg2E@>&AP2Iqfj2ye9evnk_eDSyDOuS<un2Ip(obato8M!T2cv9-GBDZ$>9v)-R@d;I}a6jQXIaT^h*zBZNEUfERX4DdtT(l=7SvOtUz7Z_PjrzB-a<!_wi@h2n)o7c%egdgl&b;VAmL0rY4b=t@Y@M}=^%#D`59G<j;)(#R#Ey-DYfGRt{O<iprLpL%I@EW=HPgN1W&pe`MbqU&=!(df;fu4Lc<X5Q%Y5`!q5N`9A7hWG)hz?8%2F~^X8ITVcJ3i(<$e&;YAwJmT&CXRy{;)eVENo*>oeTO1-0gc;imzTseaaM)g}wTLZIkr5wJf#sbFb!aa}6Yng|gV}n#ZhhuK@zrz4P2Sz-W}$6>86A_Yu_M3MWBOqE|v&uE2EnZi=K_I#-X!ne)z>i?uiA?qk6eo&C<K>++xz@kN_(;+|I}3Im6TM~9;cXeSf)0Z^blTRM6wGmFyLY>_0@eB3}qNiqQc*pRzil%ymIQPpGcr^4(+Lyo$8Uol}=jJ~nS<qqYsriSYL{k<%un}ox*b${u{BKl-wwsHrB4it%NlC!4H1>Q}D_W4i>WKjGX8@oUR<<aBM$2tnfOZZ;eKh~%CPO5PjaOBujPWBd@a*K~K!JmqV+gtYIVK!jnZ>xX~F*kOu%Vw3wOtliHagl*XFM(jR+k!P9h4QURP7bTLUUc1zKW<iMlLV3s{El=}Jpn?*L}85;XzvHg=rr`3tU3Pg&{>?KIHs8OBN05%3*XK4_qvT6f`1{UL10Yyl;NUns+dYg`*Wy2eAcseS{U=iK!oZ~IeF6LG8hO!w<TplxmW<qEzO9^p06X9*<Ux=;>;Zd#zqzCY<UIE>>N?g1y22${<k`Y=K1W9tHvXeh~_$t5J)18ofFsWHA)xi1dxp+<r5Msf(U$#hCJp^`mw$VbmqgU9=T@5?h#$27d*Vp=Lirqz=R_aw(<t?;slNtkZN22KS!|7I&vf63o^B-h;~^%4olDF%oX;fk)R+C$S^YgDp#FM(8xQq@oA3g4=GNrG>B5%6#a*}i>90EZBP%{edop81@Sw!I<}p6h#{&lmunY8E1Dmz(grT|POV?4WK5B3@+g7@PeGwIzZyHpQN$BlFeaBx@cWJ0^`6DFT)Ou0*$JN}s175A(rTem@?ad_sm1|+JYzFqMH6|l*+}H?x6MZRped6L`QR*O&w|#<uS1WF3gu~@S$CEGO9hI>lvOYok9W+|w9Z+8HdF+1yjaH`FWl-cs3%N<;W25eSaNk<G)wozwM>UifcTX>fQh{2yeWQv1_$Dm2JHZzJj{TQl`5v)$j11vwa$xmDXttf)Ig4-0Q6{mKaxK|l6k)H<xc#IIp?mX{>0qo7x4Md%&LOJnn=lkVQx%{jh<;D^@3QY81)+V04p#B)cs!K3JxP%{OdS9a<VoP7?z;$Js+I`#g|A%j%$Jn(1Wa>a9cIz#7m^1DI11B)L5+-2I=)ssK;EqiLh@s3drT5>mYt~aYyoXjg~>;u~nYO%292>)|QON>pD%d-EpfevBGa|TPa}HjewVFy{~R^!uGFwK_&0He@36=_(b$kyggaDz)c~UOINuQXcrme{ycsNBD%~(tw(<q74@NNw)snhk$G5HSLZor2Izh<ko5*jy+lXx{8R+4Toh6cDkqpy7aZMJFJ`QRD%n-7X9RXfFmeC!x)fBhRz5ioimcZ%h3JCd8VQznt9T%{tNeG@?~_F!mCH%KAX%oxud@ujzZPT?`tgTcBASvlMg7`ac)d)x`n)GnPkZy&qN;O%xJx>q_E^7^6n|pW01uV~YmTM0_cx6FTK)2CtcRlE2?&Yx)W!6z8~-Fh5oA-=F7dxu0AmPRztL8AQr4GiN|jZej{Le&Z@IkfT)$L!dDi=)+&~<y{O*wz@ntnA6wFqbGaW|wsrVM96$2@f&Xs?J9H==_-oI$Dituzw5v@unbfMrL)glPv3dafHCI1yJg5u`0<DSE({Vrdm`>!Ob`}FrfV+5y<JqLn;9kuLrYrNtb>PTq)*OYWlA*bZH&R-uen;4E`TX|Q?cpd7frNcpfM+6!ub?YsMef#21oFi4r`c|d~XTG}UDnY!o@hg>xxIHq(YZn_!LlGt`pMG)l*9=pTNdV~f-7Gq^@IhHB=R4xhgo-Q!FwHNmlz?BHEbdI36Po>N&iRcNnAeqe`!mVaJT(GP%iAmPolu`GKcR0c?CG1UKP$xzPPg&*&n@U6%si%ga0i{(KZK$Bt)sWh5#u8`fSOrnd^aS!h#=>?I#bMHX=?o^XBJ|EntvwlGUc~xOcpRtgw4ewjSGWN;GEK!X{hoVcJ!YbRJY7KF6RSHC?i*@VhoH9t6>F@o$%z)W*7m0OB7yF=~u*bKN5`Hf4xG}lu5kQd}}8kWoMxeF^dt~SAj47Ih(;+vU4n#4A1*aSr%3S4i;c+OOoDsW)zBP$sU7(U~#ObZC#@_le37oj`p*rxTN#UmJMM=dx1TC-tVfi)()fapqCpKb@<7zEa?6$z<(+9rOfK!3x*agICYO%i9KtDAl*F#GPE1ry0=m@#1t?wz=3}y%Ue437sR*L-$hJqsUAmf%K7`_+}}Rn5%YPTfnb_Vx2_*<O=8(ei|dmGF2GWr(YKWBvidY(Ib?S`;g8>j30;`p`gyi;BiF4TF)v589)Ivr`5x$mbV*t889l8G>ced!rsV}(mGMc3?4zVR@I=*e#0|vi?uEl1I!A_^Buqw$3MZ1S(dE&JlO6qchtMh0^b12Y+s;NtkpP8_R;nH@!HHCgc8QM8_80QG#RK)3gIj^*$a4cFN}?T&o+%GbzOm*y`tF^7`Yw(V085^NS&7qmzt)jucLbOPb@RKFP}zzhDL2u0oBBMtytTakx{sHK(Ehcu91KxU<NPz`lA`p7V1||-)bAn=^3+=Y034czTL')*200)
if i==6:
  def m(s,e):
    if s==e:return
    a,b,c,d=*divmod(s-1,3),*divmod(e-1,3)
    if not((a^c)&1 or (b^d)&1):return(a+c)//2*3+(b+d)//2+1
  def d(a,J,M,N,S,L):
    if J==0:L.append("".join(map(str,S)));return
    for b in range(1,N+1):
      x=m(a,b)
      if b not in S and(J==M or(not x or x in S)):S.append(b);d(b,J-1,M,N,S,L);S.pop()
  def P(N,M):global A;L,S=[],[];d(1,M,M,N,S,L);A.extend(L)
  A=[]
  for b in range(4,10):P(9,b)
  print(*A)
if i==7:
  a,b,c,e,f,s="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",[],[["."]*1025 for _ in range(1025)],0,[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)],[(4,4)]
  for l in a:b.extend([(D2[l]>>(5-i))&1 for i in range(6)])
  for i in range(9,2,-1):
    for j1,j2 in product(range(1,2**(10-i)),repeat=2):
      x,y,l=2**i*j1,2**i*j2,2**i-3
      if j1%2==0 or j2%2==0:continue
      c[y][x]="!"
      for k in range(1,l):c[y-k][x]=c[y+k][x]=c[y][x-k]=c[y][x+k]="!"
      if b[e<<2]:G(x,y+1-l,f,2)
      else:G(x+l-1,y,f,1)
      if b[(e<<2)|1]:G(x,y+1-l,f,3)
      else:G(x+1-l,y,f,1)
      if b[(e<<2)|2]:G(x,y+l-1,f,3)
      else:G(x+1-l,y,f,0)
      if b[(e<<2)|3]:G(x,y+l-1,f,2)
      else:G(x+l-1,y,f,0)
      e+=1
  while s:
    x,y=s.pop()
    for dx,dy in f:
      nx,ny=x+dx,y+dy
      if not ib(nx,ny):continue
      if c[ny][nx]=="#"or c[ny][nx]=="?":continue
      if c[ny][nx]==".":c[ny][nx]="#";continue
      s.append((nx,ny));c[ny][nx]="?"
  for x,y in product(range(1025),repeat=2):c[y][x]="."if c[y][x]=="?"else c[y][x]
  for i,v in enumerate(c):
    if 3<=i<1022:print(*v[3:-3],sep="")
if i==8:
  g=[1]*4782966
  for i,v in enumerate(g):g[i]=0 if any((i//3**(j+7))%3==(i//3**j)%3==1 for j in range(7))else 1
  for i in range(797161):print(D[sum(2**(5-j)*g[6*i+j]for j in range(6))],end="")
if i==9:
  a,b,c,e=754828306,460286996,1695327975,[20000]
  for _ in range(99999):e.append((e[-1]*a+b)%c)
  print(*e,sep=",")