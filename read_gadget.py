import numpy as np
 

#---------------------------------------------------------
#
#---------------------------------------------------------
def read_gadget(file_in):
    #--- Open Gadget file
    file = open(file_in,'rb')
    #--- Read header
    dummy = file.read(4)               
    npart         =  np.fromfile(file, dtype='i', count=6)
    massarr       =  np.fromfile(file, dtype='d', count=6)
    time          = (np.fromfile(file, dtype='d', count=1))[0]
    redshift      = (np.fromfile(file, dtype='d', count=1))[0]
    flag_sfr      = (np.fromfile(file, dtype='i', count=1))[0]
    flag_feedback = (np.fromfile(file, dtype='i', count=1))[0]
    nparttotal    =  np.fromfile(file, dtype='i', count=6)
    flag_cooling  = (np.fromfile(file, dtype='i', count=1))[0]
    NumFiles      = (np.fromfile(file, dtype='i', count=1))[0]
    BoxSize       = (np.fromfile(file, dtype='d', count=1))[0]
    Omega0        = (np.fromfile(file, dtype='d', count=1))[0]
    OmegaLambda   = (np.fromfile(file, dtype='d', count=1))[0]
    HubbleParam   = (np.fromfile(file, dtype='d', count=1))[0]
    header        = file.read(256-6*4 - 6*8 - 8 - 8 - 2*4-6*4 -4 -4 -4*8)
    dummy = file.read(4)

    #--- Particles to read
    n_all = npart[0]+npart[1]+npart[2]+npart[3]+npart[4]
    print('>>> '+ str(npart))

    print('mass = '+str(massarr[0]+massarr[1]))

    #--- Read positions
    dummy = file.read(4)
    pos = np.fromfile(file, dtype='f', count=n_all*3)
    file.close()

    #--- Rearrange data
    pos = pos.reshape((n_all,3))
    #--- Only dark matter particles
    #x = pos[npart[0]:npart[0]+npart[1],0]
    #y = pos[npart[0]:npart[0]+npart[1],1]
    #z = pos[npart[0]:npart[0]+npart[1],2]

    return pos, redshift


PATH = 'RUNS/00-00-00/OUT/'

pos, redshift = read_gadget(PATH + 'run_150')


#--- Cut a part of the box
sub = (pos[:,2] < 8000).nonzero()[0]


np.save('run_150.npy', pos)
np.save('run_150_sub.npy', pos[sub,:])



#print(len(x))
#print(x[0:10])








