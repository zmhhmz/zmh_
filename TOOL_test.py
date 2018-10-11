import os

filename ='CAVEmainRNN.py'
outname = 'CAVEmainRNN_temp.py'

keywords={
'F': 'tf.app.flags.DEFINE_integer(\'FixnetLTest\','
'T': 'tf.app.flags.DEFINE_string(\'test_dir\','
}

Experiments =[{
    'F':4,
    'T':'temp/train_RNNv2_10_3_4_20epo/'
},{
    'F':5,
    'T':'temp/train_RNNv2_10_3_5_20epo/'
},{
    'F':6,
    'T':'temp/train_RNNv2_10_3_6_20epo/'
},{
    'F':7,
    'T':'temp/train_RNNv2_10_3_7_20epo/'
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











