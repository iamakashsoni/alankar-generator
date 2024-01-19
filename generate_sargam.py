def generate_sargam(swar_notation):
    swar=["सा","रे","ग","म","प","ध","नि","सां"]
    sub=""
    sub1=""
    sub2=""
    inp=str(swar_notation)
    aroh,index,avroh=[],[],[]
    count=0

    for i in inp:
        index.append(int(i))

    if 7 in index:
        ind1=index[:(len(index)//2)]
        ind2=index[(len(index)//2):]

        ar1,ar2=[],[]

        while count<=7:
        
            for i in ind1:
                sub1+=swar[i]
            ar1.append(sub1)

            if "सां" in sub1 or "सा" in sub2:
                def lastswar():
                    temps=""
                    for i in ind2:
                        temps+=swar[i]
                    if "सा" in temps:
                        ar2.append(temps)
                lastswar()
                break

            sub1=""

            for i in ind2:
                sub2+=swar[i]
            ar2.append(sub2)
        
            sub2=""
        
            for i in range(0,len(ind1)):
                if i>7:
                    break
                ind1[i]+=1

            for i in range(0,len(ind2)):
                if i<0:
                    break        
                ind2[i]-=1

            count+=1

        n=0
        for i in ar1:
            for j in range(n,len(ar2)):
                aroh.append(i+ar2[j])
                avroh.append(ar2[j]+i)
                break
            n+=1

        print("aroh= ",aroh)
        print("avroh= ",avroh)

    else:    
        while count<=7:
        
            for i in index:  #aroh
                if i>7 :
                    break
                sub+=swar[i]
            aroh.append(sub)

        
            rev=""
            for i in index:       #avroh
                rev+=swar[::-1][i]
            avroh.append(rev)

            if "सां" in sub:
                break

            sub=""
            for i in range(0,len(index)):
                index[i]+=1
            
            count+=1
    
    return aroh, avroh


