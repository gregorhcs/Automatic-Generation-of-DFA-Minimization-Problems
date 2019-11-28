from DFA                   import DFA
from DFABuilderRandomized  import build_random_minimal_dfa
from DFABuilderEnumerating import build_next_minimal_dfa
from DFAExtender           import extend_minimal_complete_dfa
from minimize_dfa          import minimize_dfa
from pdf_from_dfa          import pdf_from_dfa
from clean                 import clean_code_dir_keep_results


CONSTRUCT_RANDOM_MINIMAL_DFA = False

CONSTRUCT_ENUMERATED_MINIMAL_DFA = True


def main():

    # construct dfa

    orig_dfa = None
    
    alphabetSize = 2
    numberOfStates = 4
    numberOfAcceptingStates = 1
    minMinmarkDepth = 2
    maxMinmarkDepth = 2
    
    if CONSTRUCT_ENUMERATED_MINIMAL_DFA:

        orig_dfa = build_next_minimal_dfa(alphabetSize, numberOfStates, numberOfAcceptingStates, minMinmarkDepth, maxMinmarkDepth)

    elif CONSTRUCT_RANDOM_MINIMAL_DFA:

        orig_dfa = build_random_minimal_dfa(alphabetSize, numberOfStates, numberOfAcceptingStates, minMinmarkDepth, maxMinmarkDepth)

    else:

        orig_dfa = DFA(
            ['a','b','c','d','e'],
            ['1','2','3','4','5'],
            [
                (('1','a'),'1'),
                (('1','b'),'2'),
                (('2','c'),'4'),
                (('5','d'),'1'),
                (('2','e'),'5')
            ],
            '1',
            ['4','5']
        )

        orig_dfa = DFA(
            ['0', '1'],
            ['AD', 'B', 'CE', 'G'],
            [
                (('AD','1'),'CE'),
                (('AD','0'),'G' ),
                
                (('B' ,'0'),'CE'),
                (('B' ,'1'),'CE'),
                
                (('CE','0'),'B' ),
                (('CE','1'),'AD'),
                
                (('G' ,'0'),'B' ),
                (('G' ,'1'),'CE'),
            ],
            'AD',
            ['CE']
        )


    # extend dfa

    task_dfa, duplicate_states, unreachable_states, equiv_classes = extend_minimal_complete_dfa(orig_dfa, 2, 1)

    # test if duplication and minimization work
    
    min_dfa, min_mark_depth = minimize_dfa(task_dfa)

    # generate graphical representation of original and extended dfa

    print(duplicate_states, unreachable_states, equiv_classes)

    pdf_from_dfa(orig_dfa, "1")
    pdf_from_dfa(task_dfa, "2")
    pdf_from_dfa(min_dfa, "3")

    # clean up directory

    clean_code_dir_keep_results()


if __name__ == "__main__":

    main()
