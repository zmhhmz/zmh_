import os

filename ='CAVEmainRNN.py'
outname = 'CAVEmainRNN_temp.py'

keywords={
'H' : 'tf.app.flags.DEFINE_integer(\'HSInetL\',',
'F' : 'tf.app.flags.DEFINE_integer(\'FixnetL\',',
'T' :'tf.app.flags.DEFINE_string(\'train_dir\',',
'E' : 'tf.app.flags.DEFINE_integer(\'epoch\','

}

Experiments =[{
    'H':12,
    'F':3,
    'T':'temp/train_RNNv2_12_3_15epo/',
    'E':20
},{
    'H':14,
    'F':1,
    'T':'temp/train_RNNv2_14_1_20epo/',
    'E':20
},{
    'H':12,
    'F':1,
    'T':'temp/train_RNNv2_12_1_15epo/',
    'E':20
}]

def Process(filename,outname,key_reps):
    with open(filename, 'r') as file :
        filedata = file.read()

    lines=filedata.split('\n')
    for key_rep in key_reps:
        keyword = key_rep['keyword']
        replace = key_rep['replace']
        for i in range(len(lines)):
            if keyword in lines[i]:
                lines[i] = replace
                print(replace)

    file2=str()
    for i in range(len(lines)):
        if i!=len(lines)-1:
            file2=file2+lines[i]+'\n'
        else:
            file2=file2+lines[i]

    with open(outname, 'w+') as file:
        file.write(file2)

for exp in Experiments:
    key_reps=[]
    for key,value in exp.items():
        if type(value)!=str:
            key_reps.append({'keyword':keywords[key],'replace':keywords[key]+str(value)+','})
        else:
            key_reps.append({'keyword':keywords[key],'replace': keywords[key]+'\''+str(value)+'\','})
    Process(filename,outname,key_reps)
    os.system('python3 CAVEmainRNN_temp.py')











