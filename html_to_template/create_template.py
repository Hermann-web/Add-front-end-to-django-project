
'''
Il faut rentrer dans le fichier 'create_template', modifier la liste Name pour integrer les noms de mes fichiers html
Si je lance le programme, il me crée un nouveau fichier templare en ajoutant les gabarit {% static, {% url et %} aux bons endroits
'''

#exemples

    #exemple1
'''ce code remplace
        #-link" href="panier.html">Pani-link" href="panier.html">Pani
        #par 
        -link" href={% static "panier.html" %}>Pani-link" href={% static "panier.html" %}>Pani
'''
    
    #exemple 2
'''
        ce code remplace::href="panier.html"
                par ::href={% url "panier" %}
        ce code remplace::href="mm.png"
                par ::href={% static "mm.png" %}
        ce code remplace::href="contact.html"
                par ::src={% url "contact" %}
        ce code remplace::href="panier.png"
                par ::src={% static "panier.png" %}
        ce code evite de faire ces operations sur 
            - href={
            - href="#
            - href=""
            - href={
            - href={
            
        Après l'operation, il crée un nouveau fichier 
'''

#les données à inclure
add_gauche = "{% static "
add_gauche_url = "{% url "
add_droite = " %}"

#liste des noms des fichiers html #il faut mettre ce fichier py dans un même dossier que les teplates
#Names = ['compte', "contact", 'creation', "index", "panier","produit","Simu"]  

Names = []



import os
Files = os.listdir()
for file in Files:
    filename,extention = os.path.splitext( file)
    if extention in ['.html', '.xhtml']:
            Names.append(filename) 

#Names = ["index"]

#Names = ["creation"]


print(Names)


def operate(Liste, i, Liste_pos_gauch, state):
    
    
    #for tag in ['href', 'src', 'href ', 'src ']:
    for tag in ['href', 'src']:
        n = len(list(tag))
        if Liste[i:i+n]==list(tag):
            
            o = len (list('=\'//www.'))
            
            #dans les exceptions, je ne gere pas gencore les = + espace #je peux definir une fonction qui fait ça
            #if Liste[i+n:i+n+2]!=list('={') and Liste[i+n:i+n+6]!=list('=\"http') and Liste[i+n:i+n+3]!=list('=\"#') and Liste[i+n:i+n+3]!=list('=\"\"') and Liste[i+n:i+n+o]!=list('=\'//www.') and Liste[i+n:i+n+6]!=list('=\"www.'):
            if '={' not in Liste[i+n:i+n+4] and 'http' not in Liste[i+n:i+n+8] and '#' not in Liste[i+n:i+n+5] and '\"\"' not in Liste[i+n:i+n+5]  and 'www.' not in Liste[i+n:i+n+o+2]:
                #print( Liste[i+5])
                #Liste_pos_gauch.append(i+n)
                
                #se positionner par rapport à "
                    #mieux que Liste_pos_gauch.append(i+n+1) où on se positionne par rapport à tag
                for a in range(1,10):
                    if Liste[i+n+a]=='\"' or Liste[i+n+a]=='\'':
                        Liste_pos_gauch.append(i+n+a)
                        state = 1
                        break
                if state==0:
                    last_pos = i+n+1
                    pp = min( 20, len(Liste)-1-last_pos)
                    print('not handled1::::', ''.join( Liste[i:last_pos+pp] ) )
                
                '''print('tag =', tag,end=' ')
                print('in')
                print( ''.join(Liste[i:i+20]))
                '''
            break

    return Liste_pos_gauch, state


def main():
    for name in Names:

        print('\n')
        print('file = ',name+'.html')
        
        #importer le fichier html dans un str
        f = open(name+'.html','r')
        STR1 = f.read()
        f.close()
        #print("STR1 :")
        #print(STR1)

        #passer de str à une liste de lettres
        Liste = list(STR1)
        #print(Liste)

        #listes d'indices 
        Liste_pos_gauch = [] #liste des positions où il faut ajouter le str add_gauche_url ou add_gauche
        Liste_pos_droit = [] #liste des positions où il faut ajouter le str add_droite
        Liste_html=[] #liste de valeurs (0 ou 1) #A chaque position où il y a un fichier html, la valeur est =1. Cette liste est utilisée pour connaitre les positions où il faut mettre add_gauche_url au lieu de add_gauche


        state =0 #state =0 indique qu'on parcoure librement le fichier 
                 #state=1 indique qu'on a trouvé une position gauche et qu'on cherche une position droite 
        
        #je parcoure le fichier lettre par lettre 
        for i in range(len(Liste)):
            #si j'ai pas encore trouve un tag 
            if state ==0:
                #Il peut ne pas trouver les bons debut de tag (les règless sont strictes mais on peut etendre)
                Liste_pos_gauch, state = operate(Liste, i, Liste_pos_gauch, state)

            else:
                #Et si par hazard, il a vu un debut dont il n'a pa vu la fin alors qu'il est tombe sur un autre debut, il abandonne l'ancien debut.
                if Liste[i:i+4]==list('href') or Liste[i:i+3]==list('src'):
                    last_pos = Liste_pos_gauch.pop()
                    Liste_pos_gauch, state = operate(Liste, i, Liste_pos_gauch, state)
                    pp = min( 20, len(Liste)-1-last_pos)
                    pp2 = min( 10, last_pos)
                    print('not handled::::', ''.join( Liste[last_pos-pp2:last_pos+pp] ) )

                        
                #sinon, il voit si il a trouve une fin 
                #si il a vu un debut (via href ou src), il va trouver une fin via (.html, .css, .js, .png, jpeg, .......): Il y a autant de debut que de fin 
                else:
                    fl_tg = list(set(['.html', '.css', '.gif','.png','.jpeg', '.jpg','.js','.svg', '.jfif' ])) #liste des extensions à considerer pour passer à state =0
                    
                    for tag in fl_tg:
                        ls = list(tag)
                        n = len(ls)
                        #si je retrou l'un des extensions 
                        if Liste[i:i+n]==ls:                     
                            
                            #se positionner par rapport à "
                                #mieux que Liste_pos_droit.append(i+n+1) où on se positionne par rapport à tag
                            max1 = min( 10, len(Liste)-1-i-n)
                            for a in range(0,max1):     
                                if Liste[i+n+a]=='\"' or Liste[i+n+a]=='\'':
                                    Liste_pos_droit.append(i+n+a+1)
                                    #je stipule que j'ai trouve le tag final
                                    state = 0
                                    
                                    #si j'apell un templeate html, il faut mettre url et enlever l'extention .html 
                                    is_html = 1 if tag=='.html' else 0
                                    Liste_html.append(is_html)
                                    break 
                                
                            if state==1:
                                last_pos = Liste_pos_gauch.pop()
                                pp = min( 20, len(Liste)-1-last_pos)
                                pp2 = min( 10, last_pos)
                                print('not handled::::', ''.join( #Liste[last_pos-pp2:last_pos+pp] ) )
                                Liste[last_pos-pp2:a+1] ) )
                            
                             
                            
                            
                            
                            break
                

            
        #print(Liste_pos_gauch)
        #print(Liste_pos_droit)

        #ici, on insere les données dans le fichier 
        if len(Liste_pos_gauch)==len( Liste_pos_droit):
            N = len( Liste_pos_droit)
            #je parcoure l'ensemble des positions 
            for i in range(N-1,-1,-1):
                print('handled::::', ''.join( Liste[Liste_pos_gauch[i]:Liste_pos_droit[i]] ) ,end=' ')
                #j'ajoute %}
                Liste.insert( Liste_pos_droit[i], add_droite) 
                
                #j'ajoute {% url 
                if Liste_html[i]==1:
                    #si j'apell un templeate html, il faut mettre url et enlever l'extention .html
                    Liste.insert( Liste_pos_gauch[i], add_gauche_url)
                #j'ajoute {% static
                else:
                    Liste.insert( Liste_pos_gauch[i], add_gauche) 
                tl = Liste_pos_droit[i]- Liste_pos_gauch[i]
                for _ in range(max(0,20- tl)):
                    print( ' ',end='')
                print('to ', ''.join( Liste[Liste_pos_gauch[i]:Liste_pos_droit[i]+ len(add_droite)] ) )
                
                
                
        else:
            print("wtf--------------")
        #enlever les .html 
        for i in range(len(Liste)):
            n = len(list('.html'))
            if Liste[i:i+n]==list('.html'):
                for j in range(i+n-1,i-1,-1):
                    trash = Liste.pop(j)
        
        STR2 = ''.join(Liste)
        #print("STR2 :")
        #print(STR2)

        #exporter le fichier html 
        f = open(name+'_.html','w')
        f.write(STR2)
        f.close()

if __name__ == '__main__':
    import sys
    import os 
    print(len(sys.argv))
    #file = sys.argv[1]
    main()
    