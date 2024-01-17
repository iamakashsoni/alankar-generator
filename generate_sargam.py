def generate_sargam(swar_notation):
    swar=["सा","रे","ग","म","प","ध","नि","सां"]
    sub=""
    inp=str(swar_notation)
    aroh,index,avroh=[],[],[]
    count=0

    for i in inp:
        index.append(int(i))
        
    while count<=7:
        for i in index: 
            if i>7 :
                break
            sub+=swar[i]
        aroh.append(sub)

        
        rev=""
        for i in index:     
            rev+=swar[::-1][i]
        avroh.append(rev)

        if "सां" in sub:
            break

        sub=""
        for i in range(0,len(index)):
            index[i]+=1
            
        count+=1
    
    return aroh, avroh


