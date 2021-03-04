import numpy as np 
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script analyzes a user given molden file and outputs the contribution of AOs in MOs.")
    parser.add_argument("molden_file", help="The molden file to analyze.")
    args = parser.parse_args()
    moldenfilename = args.molden_file
    path, file = os.path.split(moldenfilename)
    
    f = open(file, "r")
    searchlines = f.readlines()
    f.close()
    atoms_inf = []
    atoms_n = [] 
    Atm_Orb = []
    MOs_lines = []
    MO_occ = []
    MO_spin = []
    MO_en = []
    MO_sym = []
    ex1 = []
    ex2 = []
    RES_sum = []
    RES_COEF_SQR_PER_SUM = []
    MO_coefficients = []
    MO_orbitals = []

    orbs = [" s ", " S ", " p ", " P ", " d ", " D "," f ", " F ", " g ", " G ", " h ", " H "]

    for i, line in enumerate(searchlines):
        if "[Atoms]" in line: 
            for j, line in enumerate(searchlines): 
                if "[GTO]" in line:
                    for l in searchlines[i+1:j]:
                        atoms_inf.append(l.strip())
    k = 0 
    for i, line in enumerate(searchlines):
        if "[GTO]" in line: 
            for j, line in enumerate(searchlines): 
                if "[MO]" in line:
                    for l in searchlines[i+1:j]:
                        if len(l.split()) > 2: 
                            if l.split()[0] == "s" or  l.split()[0] == "S": 
                                s = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]
                                Atm_Orb.append(s)
                            if l.split()[0] == "p" or  l.split()[0] == "P": 
                                px = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"x"
                                Atm_Orb.append(px)
                                py = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"y"
                                Atm_Orb.append(py)
                                pz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"z"
                                Atm_Orb.append(pz)
                            if l.split()[0] == "d" or  l.split()[0] == "D":
                                dxx = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xx"
                                Atm_Orb.append(dxx)
                                dyy = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"yy"
                                Atm_Orb.append(dyy)
                                dzz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"zz"
                                Atm_Orb.append(dzz)
                                dxy = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xy"
                                Atm_Orb.append(dxy)
                                dxz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xz"
                                Atm_Orb.append(dxz)
                                dyz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"yz"
                                Atm_Orb.append(dyz)
                            if l.split()[0] == "f" or  l.split()[0] == "F":
                                fxxx = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xxx"
                                Atm_Orb.append(fxxx)
                                fyyy = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"yyy"
                                Atm_Orb.append(fyyy)
                                fzzz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"zzz"
                                Atm_Orb.append(fzzz)
                                fxyy = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xyy"
                                Atm_Orb.append(fxyy)
                                fxxy = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xxy"
                                Atm_Orb.append(fxxy)
                                fxxz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xxz"
                                Atm_Orb.append(fxxz)
                                fxzz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xzz"
                                Atm_Orb.append(fxzz)
                                fyzz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"yzz"
                                Atm_Orb.append(fyzz)
                                fyyz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"yyz"
                                Atm_Orb.append(fyyz)
                                fxyz = (atoms_inf[k]).split()[0] +" "+ str(k+1) + "     " + l.split()[0]+"xyz"
                                Atm_Orb.append(fxyz)
                        if len(l.split()) == 0:
                            if k+1 < len(atoms_inf):
                                k += 1 

    indx = 0
    for i, line in enumerate(searchlines):
        if "Sym=" in line: 
            if float(searchlines[i+3].split()[1]) > 0.0:
                #print(i, searchlines[i+1], searchlines[i+2], searchlines[i+3]) #line.split()[0]
                MOs_lines.append(i)
                MO_occ.append(searchlines[i+3].split("=")[1])
                MO_spin.append(searchlines[i+2].split("=")[1])
                MO_en.append(searchlines[i+1].split("=")[1])
                MO_sym.append(searchlines[i].split("=")[1])

    path = os.path.abspath(os.getcwd())
    open_name = f'{os.path.basename(f.name.split(".")[0])}.txt'
    out = open(open_name, 'w')
    print(" ********************************" , file=out)
    print(" |      ++  MOldenizer  ++      |" , file=out)
    print(" |      ++++++++++++++++++      |" , file=out)
    print(" |      By Amir Mirzanejad      |" , file=out)
    print(" |    mirzanejad2004@gmailcom   |" , file=out)
    print(" |                              |" , file=out)
    print(" |    &  Olajumoke Dunsin       |" , file=out)
    print(" |  olajumoke.dunsin@gmail.com  |" , file=out)
    print(" |                              |" , file=out)
    print(" |         Feb. 2021            |" , file=out)
    print(" |  University of Nevada, Reno  |" , file=out)
    print(" ********************************" , file=out)
    print(" \n" , file=out)
    print(F' Input File:  {path}/{os.path.basename(f.name)}', file=out)
    print(F' Output File: {path}/{os.path.basename((f.name).split(".")[0])}.txt', file=out)
    print(" \n" , file=out)
    print(" Attention for unrestricted input files:" , file=out)
    print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" , file=out)
    print(" + Alpha-spin orbitals are listed prior to Beta-spin orbitals +" , file=out)
    print(" ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" , file=out)
    for ii in range(0, len(MOs_lines)):
        if int(MOs_lines[ii]) <= int(MOs_lines[-1]):
            dx = MOs_lines[1] - MOs_lines[0]
            for line in searchlines[int(MOs_lines[ii]+4):int(MOs_lines[ii]+dx)]: 
                float_formatter = "{:.1f}".format
                MO_coefficients.append((str(float(line.split()[1])**2)))
                MO_orbitals.append(Atm_Orb[int(line.split()[0])-1])
            sqr_sum = np.sum(list(map(float, MO_coefficients)))
            print("\n", file=out)
            print("*************************************************", file=out)
            print(F"  Sum over coefficients in MO# {ii+1}  is: ", '{:.2f}'.format(float(sqr_sum)), file=out)
            print(F"  En. {str(MO_en[ii]).split()[0]} H, {float(str(MO_en[ii]).split()[0])*630} kcal/mol", file=out)
            print(F"  OCC. {'{:.2f}'.format(float(MO_occ[ii]))}", file=out)
            print(F"  Sym. {str(MO_sym[ii]).split()[0]}", file=out) 
            if float(MO_occ[ii]) > 1.00:
                print(F"  Spin {str(MO_spin[ii]).split()[0]} and Beta", file=out)
            else: 
                print(F"  Spin {str(MO_spin[ii]).split()[0]}", file=out)
            perc = (list(map(float, MO_coefficients))/sqr_sum)*100
            perc_output = ["%.2f" % elem for elem in perc]
            ex1.append(perc_output)
            v1 = np.array(MO_orbitals).reshape(-1,1)
            v2 = np.array(ex1).reshape(-1,1)
            final_matrix = np.array(np.concatenate((v1,v2), axis=1))
            sort1 = final_matrix[np.argsort(final_matrix[:, 1])[::-1]]
            np.set_printoptions(threshold=np.inf)
            print("*  Atom * Orb *** Percent ***", file=out)
            print("-----------------------------", file=out)
            #print(sqr_sum)
            for a in sort1:
                if float(a[1]) > 1: 
                    for elem in a:
                        print("   {}".format(elem).ljust(15), end="", file=out)
                    print(end="\n", file=out)
                    print("-----------------------------", file=out)
            print(F"Molecular Orbital {ii+1} out of {len(MOs_lines)} is done!")
            MO_coefficients = []
            ex1 = []
            MO_orbitals = []
    print("*** End of the file ***", file=out)
    print("*************************************************", file=out)
    print("DONE!")
    print("\x1b[6;30;42m" + F'Your output file is written in {path}/{os.path.basename((f.name).split(".")[0])}.txt' + "\x1b[0m")
    out.close()
