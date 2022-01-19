#auto generate different Capa Value&Mos Length
import os
out = [[0 for i in range(4)] for j in range(12)]
# print(out,'outgen')
out[0]=['L   ','C       ','Iavg             ','Pavg   ']
L=1
C=0.01
count=1
while count<12:
    #f=open('./DRAM%s'%count+'.sp', mode='x') #./ means local file
    if count==1:
        L=1
        C=0.01
    else:
        if count==2:
            L=0
        L=L+10
        C=7**(0.1*(count-1))
    filename=str(L)+'n'+'_'+'%.2f'%C+'fF' #
    #print(format(1.23456, '.2f'))
    f = open('./DRAM%s' % filename + '.sp', mode='w')
    runtime=100
    if L>= 70:
        runtime=100000

    f.write("SPICE LAB4P1 1T-DRAM\n.include tsmc025.inc\n.param vdd=0.7\nvs vs 0 'vdd/2'\nm0 vs 0 vc 0 CMOSN L=%d"%L+"n W=120e-9\nc1 vc 0 %f"%C+"fF\n\
.IC V(vc)='vdd'\n.option post=2 nomod\n.op\n.tran .01ns %d"%runtime+"ns\n.print V(vc)\n.OPTION Post Brief NoMod probe measout\n.measure tran RTL TRIG AT=0 TARG v(vc) VAL=0.55 FALL=1\n\
.measure tran Iavg AVG I(c1) from 0 to 'RTL'\n.measure tran Pavg AVG P(c1) from 0 to 'RTL'\n.end")
    f.close()

    hspicename='./DRAM%s' % filename + '.sp'
    os.system(r'hspice -i %s'% hspicename)
    # print(filename,'filename')

    # file_mt0 = open('./DRAM%s' % filename + '.mt0', mode='r')
    file_mt0 = open('DRAM%s' % filename + '.mt0', mode='r')
    file_mt0_read = file_mt0.read()
    file_mt0_read=file_mt0_read.split('\n')
    # print(file_mt0_read,'file_mt0_read')
    file_mt0_read_ValueLine=file_mt0_read[4]
    file_mt0_read_ValueLine_split=file_mt0_read_ValueLine.split()
    print(file_mt0_read_ValueLine_split,'file_mt0_read_ValueLine_split')
    out[count][0]=str(L)+'n'
    C='%.2f'%C
    out[count][1]=str(C)+'fF'

    out[count][2]=file_mt0_read_ValueLine_split[1]+'A'

    out[count][3]=file_mt0_read_ValueLine_split[2]+'W'


    f_out = open('DRAM.txt', mode='w')
    for item1 in out:
        for item in item1:
            f_out.write(str(item)+' ')
        f_out.write('\n')




    count=count+1
