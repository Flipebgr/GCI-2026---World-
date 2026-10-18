import numpy as np

notes_students = np.array([
    [75, 60, 82, 80],
    [90, 73, 75, 85],
    [82, 92, 80, 63]])

#[0,:] - English
#[1,:] - Math
##[2,:] - Spanish
#coluna_Aluno_a = notes_students[:,0] # seleciona a primeira coluna (índice 0) da matriz, que corresponde às notas do aluno A em todas as disciplinas.
#coluna_Aluno_d = notes_students[:,3] # seleciona a quarta coluna (índice 3) da matriz, que corresponde às notas do aluno D em todas as disciplinas.
#note_max_general_a = np.max(coluna_Aluno_a,axis=0)
#note_max_general_d = np.max(coluna_Aluno_d,axis=0)

#print("A nota máxima do aluno A é:", note_max_general_a)
#print("A nota máxima do aluno D é:", note_max_general_d)


#notes_english = notes_students[0,:]
#max_note_english = np.max(notes_english)
#print("A nota máxima em inglês é:", max_note_english)

#notes_math = notes_students[1,:] # seleciona a segunda linha (índice 1) da matriz, que corresponde às notas de matemática de todos os alunos.
#max_note_math = np.max(notes_math) 
#print("A nota máxima em matemática é:", max_note_math)

#notes_spanish = notes_students[2,:] # seleciona a terceira linha (índice 2) da matriz, que corresponde às notas de espanhol de todos os alunos.
#max_note_spanish = np.max(notes_spanish)
#print("A nota máxima em espanhol é:", max_note_spanish)

#reshape() - mudar a forma da matriz

notes_students = notes_students.reshape(4,3)
print("Matriz de notas dos alunos após o reshape:")
print(notes_students)
print("A forma da matriz após o reshape é:", notes_students.shape)