import string, sys,os

# IN parameter:
#      fastafile: file pointer
# RETURN:
#      [[id,seq],...]

def fasta(fastafile):
    id_seq_list =[]
    for record in string.split('\n'+string.strip(fastafile.read()) ,'\n>'):
        if record != '':
            data = string.split(record,'\n')
            id = data[0] #id is line'>"
            seq = string.strip(string.join(data[1:],''))
            id_seq_list.append([id,seq])
    fastafile.close()
    return id_seq_list

def fasta_dic(fastafile):
    id_seq_dic ={}
    id_list = []

    line = fastafile.readline()
    seq_list =[]
    id =''
    while (line!=''):
        if line[0] =='>':
            if len(seq_list) == 0 and id =='':
                id = string.strip(line[1:])  #id is whole line
            else:
                seq = string.join(seq_list,'')
                seq = string.upper(string.strip(string.replace(seq,' ','')))
                seq = string.upper(string.strip(string.replace(seq,'\n','')))
                id_seq_dic[id] = seq
                id_list.append(id)
                id = string.strip(line[1:])  #id is whole line
                seq_list =[]
        else:
            seq_list.append(line)
        line = fastafile.readline()

    if len(seq_list)==0 and id =='':
        pass
    else:
        seq = string.join(seq_list,'')
        seq = string.upper(string.strip(string.replace(seq,' ','')))
        seq = string.upper(string.strip(string.replace(seq,'\n','')))
        id_seq_dic[id] = seq
        id_list.append(id)

    fastafile.close()
    return id_seq_dic, id_list

def fasta_id_list(fastafile):
    #id_seq_dic ={}

    line = fastafile.readline()
    id_list =[]
    id =''
    while (line!=''):
        if line[0] =='>':
            id = string.strip(line[1:])  #id is whole line
            id_list.append(id)
        line = fastafile.readline()


    #fastafile.close()
    return id_list



def generate_fasta (fasta_dic, fout):  #fout : ptr to output file
    for key in fasta_dic.keys():
        fout.write('>'+key+'\n')
        fout.write(fasta_dic[key]+'\n')
    fout.close()
    return

# qiang sun: use this function to generate the fasta file in order
def generate_fasta_in_order(fasta_dic, ordered_ids, fout):
    for id in ordered_ids:
        if not fasta_dic.get(id) == None:
            fout.write('>'+id+'\n')
            seq = fasta_dic[id]
            
            cycles = len(seq)/60
            for i in range(cycles):
                fout.write(seq[i*60:(i+1)*60]+'\n')
            last = len(seq)%60
            if last != 0:
                fout.write(seq[-last:]+'\n')
    fout.close()
    return


#all files are in fasta format
def find_fasta(fseq, fid, fout):
    id_dic = fasta_dic(fid)
    seq_dic = fasta_dic(fseq)

    temp_dic ={}
    keys = id_dic.keys()
    for id in keys:
        try:
            temp_dic[id] = seq_dic[id]
        except KeyError:
            print "no seq in fseq file"

    generate_fasta(temp_dic, fout)

#check if file fseq is in the correct fasta format
#return 0 as fail
#return 1 as success
def check_format_fasta(fseq):
    FAIL = 0
    SUCCESS = 1
    
    began =0
    while (began == 0 ):
        line = fseq.readline()
        if line == '':
            return FAIL
        elif line == '\n':
            continue
        elif string.strip(line[0]) != '>':
            return FAIL
        else:
            began = 1

    idline = 0
    sequence=""
    while (1):
        line = fseq.readline()
        if line == '':
            break
        if (idline ==0):
            if string.strip(line) == '':
                if sequence != "":
                    idline = not (idline)
                    sequence =""
                continue
            elif string.find(line, '>') != -1:
                idline = not(idline)
                sequence = ""
            else:
                sequence = "a"
        if (idline == 1):
            if string.strip(line) == '':
                continue
            elif string.find(line, '>') != 0:
                return FAIL
            else:
                idline = not(idline)
                
    if ( idline !=1 and sequence !="") or (idline ==1 and sequence ==""):
        return SUCCESS
    
    return FAIL

#converting all sequences into UPPER case
def ToUpper(seq_dic):
    for id in seq_dic.keys():
        seq = seq_dic[id]
        seq_dic[id] = string.upper(seq)

