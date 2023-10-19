from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
import smtplib
from email.message import EmailMessage
import time
import numpy as np
from PIL import Image
import re
import sys
sys.path.insert(0, '/home/sanket/Django/Sanket')
from Sanket.models import result_model
from Sanket import views
from django.contrib.auth.models import User
options = Options()
options.headless = False
driver = Firefox(executable_path = r'/home/sanket/Django/PMtk-20220215T094451Z-001/PMtk/geckodriver',options=options)

ins = list(result_model.objects.filter(jobid = result_model.objects.all()[len(result_model.objects.all())-1].jobid))
user = list(User.objects.filter(result_model__jobid = result_model.objects.all()[len(result_model.objects.all())-1].jobid))
print("user:",user)
class Example_inputs:
    def __init__(self):
        self.Job_name = ins[len(ins)-1].jobname
        self.Email = user[len(user)-1].email
        # self.Email = 'riya@students.iisertirupati.ac.in'
        self.AlphaFold_input = ins[len(ins)-1].Q_P
        # sequence
        #self.Protein_Sequence = ins[len(ins)-1].Q_P_S
        self.Protein_Sequence = 'MSGVRGLSRLLSARRLALAKAWPTVLQTGTRGFHFTVDGNKRASAKVSDSISAQYPVVDHEFDAVVVGAGGAGLRAAFGLSEAGFNTACVTKLFPTRSHTVAAQGGINAALGNMEEDNWRWHFYDTVKGSDWLGDQDAIHYMTEQAPAAVVELENYGMPFSRTEDGKIYQRAFGGQSLKFGKGGQAHRCCCVADRTGHSLLHTLYGRSLRYDTSYFVEYFALDLLMENGECRGVIALCIEDGSIHRIRAKNTVVATGGYGRTYFSCTSAHTSTGDGTAMITRAGLPCQDLEFVQFHPTGIYGAGCLITEGCRGEGGILINSQGERFMERYAPVAKDLASRDVVSRSMTLEIREGRGCGPEKDHVYLQLHHLPPEQLATRLPGISETAMIFAGVDVTKEPIPVLPTVHYNMGGIPTNYKGQVLRHVNGQDQIVPGLYACGEAACASVHGANRLGANSLLDLVVFGRACALSIEESCRPGDKVPPIKPNAGEESVMNLDKLRFADGSIRTSELRLSMQKSMQNHAAVFRVGSVLQEGCGKISKLYGDLKHLKTFDRGMVWNTDLVETLELQNLMLCALQTIYGAEARKESRGAHAREDYKVRIDEYDYSKPIQGQQKKPFEEHWRKHTLSYVDVGTGKVTLEYRPVIDKTLNEADCATVPPAIRSY'
        self.MSAfile = r'D:\protein master toolkit\.ipynb_checkpoints\MSAfile.txt'
        self.Fasta = '>' + self.AlphaFold_input + '\n' + self.Protein_Sequence
        self.Password = 'IT_vt446'
        self.MSfile = r"/home/sanket/Django/PMtk-20220215T094451Z-001/PMtk/MultipleSequencefile.txt"
        # PDB options
        #self.PDBfile = r"/home/sanket/Django/4hhb.pdb"
        if ins[len(ins)-1].PDB :
            self.PDBfile = r'/home/sanket/Django/Sanket/Sanket'+r'{}'.format(ins[len(ins)-1].PDB.url)
        self.Protein_chain = 'A'
        self.Modeller_licence_keys = 'MODELIRANJE'
        self.Mutation_list = r'/home/sanket/Django/PMtk-20220215T094451Z-001/PMtk/Expresso.text'
        self.Single_mutation = 'E346K'
        self.Forcefields = 'C-alpha'
        self.ProteinDNA_complex = r"D:\PMtk\2A0I.pdb"
        # Docking Inputs
        self.Ligand_file = r'D:\protein master toolkit\Website\_2cha.pdb'
        self.Ligand_chain = 'A'
        self.Peptide_seq = 'HHHHHHHSFGDSF'
        self.Peptide_Fasta = '>' + 'Peptide_Sequence' + self.Peptide_seq
        self.Nucleicacid_seq = 'TTTGGGGTTGGTCAAATGAATCGGATGAAATTAAGAAAGGATGGGCTGGAATTCAAGGTATTCCGCGACAAGTA'
        self.Nucleicacid_fasta = '>' + 'Nucleic_Acid' + '\n' + self.Nucleicacid_seq
        self.Small_molecule_sdf_file = r'D:\protein master toolkit\Website\Conformer3D_CID_2244.sdf'
        # emailreport
        self.sender = 'asap@labs.iisertirupati.ac.in'
        self.password = 'Hussain@1308'


#
# class Dependency:
#     def Captcha_retrieve(self):
#         # zoom to captcha frame
#         driver.execute_script('document.body.style.MozTransform = "scale(6)";')
#         driver.execute_script('document.body.style.MozTransformOrigin = "center top";')
#         time.sleep(4)
#         # take ss and save as png
#         image = driver.save_screenshot('autodock_captcha.png')
#         # read ss
#         img = mpimg.imread('autodock_captcha.png')
#         # plot ss
#         imgplot = plt.imshow(img)
#         plt.figure(figsize=(100, 100))
#         plt.show()
ex = Example_inputs()
class Sequence:
    # iTasseronline
    def ITASSER(self):
        start = time.time()
        driver.get("https://zhanggroup.org/I-TASSER/")
        driver.implicitly_wait(10)
        Sequence_input = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/ul[1]/table/tbody/tr/td/form/textarea")
        Sequence_input.send_keys(ex.Protein_Sequence)
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/ul[1]/table/tbody/tr/td/form/p[2]/input").send_keys(
            'amogh@students.iisertirupati.ac.in')
        password = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/ul[1]/table/tbody/tr/td/form/p[3]/input")
        password.send_keys(ex.Password)
        Submit = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/ul[1]/table/tbody/tr/td/form/p[9]/input[1]")
        Submit.click()
        # print(Get_confirmtion.text)
        # report
        name = 'I-TASSER online : Protein Structure Prediction'
        inputs = ex.Protein_Sequence + '\n' + ex.Password
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'ITASSER' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # AlphaFold_Protein_Structure_Database
    def AlphaFold(self):
        start = time.time()
        driver.get("https://alphafold.ebi.ac.uk/")
        driver.implicitly_wait(10)
        Input = driver.find_element(By.XPATH, "//*[@id='searchitem']")
        Input.send_keys(ex.AlphaFold_input)
        Enter_Search = driver.find_element(By.XPATH,
                                           "/html/body/div[1]/app-root/app-header/div/div[2]/div/div/div[2]/app-header-search/button/span")
        Enter_Search.click()
        time.sleep(1)
        # report
        name = 'AlphaFold Database : AI enabled Predicted Structure for Human Proteins'
        inputs = ex.AlphaFold_input
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Alpha Fold ' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # interpro
    def interpro(self):
        start = time.time()
        driver.get('https://www.ebi.ac.uk/interpro/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[3]/div[4]/div/div/div/div/div/div/form/div[1]/div/div[1]/div/div/div/div/div['
                            '2]/div').send_keys(
            ex.Protein_Sequence)
        time.sleep(5)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div[3]/div[4]/div/div/div/div/div/div/form/div[1]/div/div[4]/div[1]/input[1]').send_keys(
            Keys.ENTER)
        time.sleep(4)
        # report
        name = 'Interpro : Predicts Protein Function Prediction'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'interpro' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # flDPnnS
    def flDPnnS(self):
        start = time.time()
        driver.get('http://biomine.cs.vcu.edu/servers/flDPnn/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/textarea').send_keys(ex.Fasta)
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/input[4]').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        confirmation = driver.find_element(By.XPATH, '/html/body/div/div[2]')
        with open('flDPnnS.text', 'w') as f:
            f.write(confirmation.text)
        # report
        name = 'flDPnn : Employs neural network to predict Disorder prediction and Disorder binding sites in the protein'
        inputs = ex.Fasta
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        driver.switch_to.window(driver.window_handles[0])
        end = time.time() - start
        print('*' * 50 + 'flDPnn' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # flDPnnM
    def flDPnnM(self):
        start = time.time()
        driver.get('http://biomine.cs.vcu.edu/servers/flDPnn/')
        driver.implicitly_wait(10)
        msfile = open(ex.MSfile, 'rt')
        k = msfile.read()
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/textarea').send_keys(k.strip('\n'))
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/input[4]').click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        confirmation = driver.find_element(By.XPATH, '/html/body/div/div[2]')
        with open('flDPnnM.text', 'w') as f:
            f.write(confirmation.text)
        # report
        name = 'flDPnn : Employs neural network to predict Disorder prediction and Disorder binding sites in the protein'
        inputs = ex.MSfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        driver.switch_to.window(driver.window_handles[0])
        end = time.time() - start
        print('*' * 50 + 'flDPnn' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # CoeViz2
    def CoeViz2(self):
        start = time.time()
        driver.get('https://research.cchmc.org/CoevLab/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[1]/div[2]/p[1]/label/input').send_keys(
            ex.AlphaFold_input)
        driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[1]/div[2]/p[2]/label/textarea').send_keys(
            ex.Protein_Sequence)
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/form/div/div[1]/div[2]/div[2]/fieldset/p[2]/select/option[2]').click()
        driver.find_element(By.XPATH, '/html/body/div[1]/form/div/div[1]/div[2]/div[1]/div[1]/a').click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        k = driver.current_url
        if k == 'https://research.cchmc.org/CoevLab/cgi-bin/coevlab.cgi':
            time.sleep(50)
        else:
            pass
        # report
        name = 'CoeViz-2 : Give the Covariance analysis'
        inputs = ex.AlphaFold_input + ' ,  ' + ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        driver.switch_to.window(driver.window_handles[0])
        end = time.time() - start
        print('*' * 50 + 'CoeViz2' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # serp Server
    def serp(self):
        start = time.time()
        driver.get('http://services.mbi.ucla.edu/SER/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[2]/table/tbody/tr/td[1]/form/div/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/input').send_keys(
            ex.AlphaFold_input)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[2]/table/tbody/tr/td[1]/form/div/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/input').send_keys(
            ex.Email)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[2]/table/tbody/tr/td[1]/form/div/table/tbody/tr/td/table/tbody/tr/td[1]/textarea').send_keys(
            ex.Protein_Sequence)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[2]/table/tbody/tr/td[1]/form/div/table/tbody/tr/td/table/tbody/tr/td[1]/input[2]').click()
        driver.find_element(By.XPATH,
                            '/html/body/div/div[2]/table/tbody/tr/td[1]/form/div/table/tbody/tr/td/table/tbody/tr/td[1]/input[5]').click()
        time.sleep(5)
        confirmation = driver.find_element(By.XPATH, '/html/body/div/div[2]/b')
        # report
        name = 'SerP Server : Predicts Surface entroy of the protein'
        inputs = ex.Protein_Sequence
        status = confirmation.text
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'serp Server' + '*' * 50)
        return name, inputs, status, url, ExTime, end

        # xTAL pred

    def xtal_pred(self):
        start = time.time()
        driver.get('https://xtalpred.godziklab.org/XtalPred-cgi/xtal.pl')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/form[1]/textarea').send_keys(ex.Protein_Sequence)
        driver.find_element(By.XPATH, '/html/body/form[1]/label[1]/input').click()
        driver.find_element(By.XPATH, '/html/body/form[1]/input[1]').send_keys(ex.Email)
        driver.find_element(By.XPATH, '/html/body/form[1]/label[2]/input').click()
        driver.find_element(By.XPATH, '/html/body/form[2]/p/input[1]').click()
        confirmation = driver.find_element(By.XPATH, '/html/body/table[1]/tbody/tr/td[2]/b')
        # report
        name = 'xtal Server : Prediction of Protein crystilizability'
        inputs = ex.Protein_Sequence
        status = confirmation.text
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'serp Server' + '*' * 50)
        return name, inputs, status, url, ExTime, end

        # reactome pathway data base

    def reactome(self):
        start = time.time()
        driver.get('https://reactome.org/')
        driver.implicitly_wait(10)
        Input = driver.find_element(By.XPATH, '//*[@id="local-searchbox"]')
        Input.send_keys(ex.AlphaFold_input)
        submit = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/form/button').click()

        time.sleep(2)
        name = 'Reactome :  Scientific Literature database for proteins'
        inputs = ex.AlphaFold_input
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'reactome pathway data base ' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    def swiss(self):
        start = time.time()
        driver.get('https://swissmodel.expasy.org/interactive')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="id_target"]').send_keys(ex.Fasta)
        driver.find_element(By.XPATH, '//*[@id="id_project_title"]').send_keys(ex.Job_name)
        time.sleep(4)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/form/div[10]/div[2]').click()
        time.sleep(5)
        confirmation = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/strong/pre')
        # print(confirmation.text)
        time.sleep(2)
        name = 'Swiss Template Search : Provides the Similar protein templates to your query protein sequence'
        inputs = ex.Fasta
        status = 'Submitted'
        url = confirmation.text + '\n' + driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Swiss Model Template Search ' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    def PDBflex(self):
        start = time.time()
        driver.get('https://pdbflex.org/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="parameterInput"]').send_keys(ex.Protein_Sequence)
        driver.find_element(By.XPATH, '//*[@id="getSequenceClusterButton"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/ul/li/button').click()
        time.sleep(4)
        name = 'PDB flex :  PDBFlex database explores the intrinsic flexibility of protein structures by analyzing structural variations between different depositions and chains in asymmetric units of the same protein in PDB'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'PDBflex' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Consurf PDB method not working
    def Consurf(self):
        start = time.time()
        driver.get("https://consurf.tau.ac.il/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[2]/label/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[2]/div[1]/label/input").click()
        time.sleep(1)
        driver.find_element(By.ID, 'pdb_file_field').click()
        time.sleep(1)
        driver.find_element(By.ID, 'pdb_file_field').send_keys(ex.PDBfile)
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[3]/div/input[4]").click()
        if ex.Protein_chain == 'null':
            No_MSA = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[3]/div[1]/div[2]/label/input")
            No_MSA.click()
        elif ex.Protein_chain == 'A':
            Chain = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[2]/select/option[2]")
            Chain.click()
            No_MSA = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[3]/div[1]/div[2]/label/input")
            No_MSA.click()
        elif ex.Protein_chain == 'B':
            Chain = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[2]/select/option[3]")
            Chain.click()
            No_MSA = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[3]/div[1]/div[2]/label/input")
            No_MSA.click()
        elif ex.Protein_chain == 'C':
            Chain = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[2]/select/option[4]")
            Chain.click()
            No_MSA = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[3]/div[1]/div[2]/label/input")
            No_MSA.click()
        else:
            No_MSA = driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div[3]/div[1]/div[2]/label/input")
            No_MSA.click()
        driver.find_element(By.XPATH, "//*[@id='auto_select']").click()
        driver.find_element(By.XPATH, '//*[@id="qtitle"]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[6]/div[8]/input').send_keys(ex.Email)
        time.sleep(1)
        Submit = driver.find_element(By.CSS_SELECTOR, "#General_fields > input:nth-child(14)")
        Submit.click()
        time.sleep(8)
        confirmation = driver.find_element(By.CSS_SELECTOR, ".container")
        with open('Consurf.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Consurf Server :  Analyse the given protein sequence'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Consurf Server' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # mTM align
    def mTMalign(self):
        start = time.time()
        driver.get('https://yanglab.nankai.edu.cn/mTM-align/index.html')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/fieldset/div[2]/div[1]/div/div/form/div[2]/input[1]').send_keys(
            ex.PDBfile)
        driver.find_element(By.XPATH, '/html/body/div/fieldset/div[2]/div[1]/div/div/form/div[7]/input').send_keys(
            ex.AlphaFold_input)
        driver.find_element(By.XPATH, '/html/body/div/fieldset/div[2]/div[1]/div/div/form/input').click()
        submit = driver.find_element(By.XPATH, '//*[@id="submit"]')
        submit.click()
        time.sleep(4)
        #result = driver.find_element(By.XPATH, '/html/body/a[2]')
        # print(confirmation.text)
        time.sleep(2)
        name = 'mTM Align :  Multiple structure alignment automatically selects the candidates to be aligned'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'mTM Alignment' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # CUPSAT denaturant meth
    # od for all amino acids
    def CUPSAT(self):
        start = time.time()
        driver.get("http://cupsat.tu-bs.de/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div[3]/div[3]/div[2]/a').click()
        PDB_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[3]/div[2]/div[2]/form/div[2]/input")
        PDB_input.send_keys(ex.PDBfile)
        submit = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[3]/div[2]/div[2]/form/div[3]/input[3]')
        submit.click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/form/div/div[1]/div[2]/div[2]/input').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/form/div/div[4]/div[2]/div[2]/input').click()
        if ex.Protein_chain == 'A':
            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div/div[3]/form/div/div[5]/div[2]/select/option[1]').click()
        elif ex.Protein_chain == 'B':
            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div/div[3]/form/div/div[5]/div[2]/select/option[2]').click()
        else:
            pass

        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/form/div/div[6]/div[2]/input[1]').click()
        time.sleep(5)

        # get_confirmation=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/form')
        # print(get_confirmation.text)
        time.sleep(2)
        name = 'CUPSAT Structure Analysis by inducing mutation'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'CUPSAT' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # P2RANK
    def P2RANK(self):
        start = time.time()
        driver.get("https://prankweb.cz/")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="upload-pdb"]').send_keys(ex.PDBfile)
        driver.find_element(By.XPATH, '//*[@id="fileChains"]').send_keys(ex.Protein_chain)
        submit = driver.find_element(By.XPATH, '//*[@id="pdbUploadSubmit"]')
        submit.click()
        time.sleep(5)
        name = 'PrankWeb: Ligand Binding Site Prediction'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'PrankWeb: Ligand Binding Site Prediction' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # FPocket : not working
    def fPocket(self):
        driver.get('https://mobyle.rpbs.univ-paris-diderot.fr/cgi-bin/portal.py#forms::fpocket')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/table[2]/tbody/tr/td[3]/div/div[2]/div/div/div/form/fieldset[2]/div/label/input').send_keys(
            ex.Job_name)
        driver.find_element(By.XPATH,
                            '/html/body/table[2]/tbody/tr/td[3]/div/div[2]/div/div/div/form/fieldset[2]/div/fieldset[1]/div[2]/ul/li['
                            '3]/label').click()
        time.sleep(2)
        driver.find_element(By.XPATH,
                            '/html/body/table[2]/tbody/tr/td[3]/div/div[2]/div/div/div/form/fieldset[2]/div/fieldset[1]/div['
                            '2]/div/div[3]/div/table/tbody/tr/td[1]/span/input[1]').send_keys(
            ex.PDBfile)
        submit = driver.find_element(By.XPATH,
                                     '/html/body/table[2]/tbody/tr/td[3]/div/div[2]/div/div/div/table/tbody/tr/td[2]/span/input[1]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '/html').send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, '/html').send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, '/html').send_keys(Keys.ARROW_UP)
        time.sleep(1)

        Dependency.Captcha_retrieve(self)

        lol = input('enter captcha text from the screen shot:')
        driver.find_element(By.XPATH, '//*[@id="captchaSolution"]').send_keys(lol)
        driver.find_element(By.XPATH, '//*[@id="usercaptchaSubmit"]').click()
        time.sleep(5)
        confirmation = driver.find_element(By.CSS_SELECTOR,
                                           'html body#portalBody table#mainContainer tbody tr td#portalMain')
        print(confirmation.text)
        time.sleep(5)
        print(driver.current_url)
        print('*' * 50)

    # iCn3D visualization
    def iCn3D(self):
        start = time.time()
        driver.get("https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="ui-id-1"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="ui-id-14"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="div0_mn1_pdbfile_app"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="div0_pdbfile_app"]').send_keys(ex.PDBfile)
        submit = driver.find_element(By.XPATH, '//*[@id="div0_reload_pdbfile_app"]')
        submit.click()
        time.sleep(2)
        name = 'I Can See 3D : visualised and analyse structure'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'iCn3D' + '*' * 50)
        return name, inputs, status, url, ExTime, end
        # driver.find_element_by_css_selector("html body
        # div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-draggable.ui-resizable
        # div#div0_dl_mmdbid.ui-dialog-content.ui-widget-content input#div0_mmdbid").clear()
        # Input=driver.find_element_by_css_selector("html body
        # div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-draggable.ui-resizable
        # div#div0_dl_mmdbid.ui-dialog-content.ui-widget-content input#div0_mmdbid") Input.send_keys(PDBid)
        # Enter_Search=driver.find_element(By.XPATH, "//*[@id='div0_reload_mmdb']") Enter_Search.click() time.sleep(5)
        # driver.close()

    # Protein Contact Atlas
    def ProteinContactAtlas(self):
        start = time.time()
        driver.get('https://www.mrc-lmb.cam.ac.uk/rajini/index.html')
        time.sleep(3)
        driver.find_element(By.XPATH,
                            '/html/body/div[3]/div[2]/div/div/div[2]/div/div/font[2]/font/div[6]/a/h4').click()
        driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(ex.PDBfile)
        time.sleep(1)
        submit = driver.find_element(By.XPATH, '//*[@id="uploadbutton"]')
        submit.click()
        driver.implicitly_wait(180)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button').click()
        confirmation = driver.find_element(By.XPATH, '//*[@id="explanation"]')
        print(confirmation.text)
        time.sleep(2)
        name = 'Protein Contact Atlas : Interaction Profiles of the query Protein'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Protein Contact Atlas' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # PLIP protein ligand interaction profiler
    def PLIP(self):
        start = time.time()
        driver.get('https://plip-tool.biotec.tu-dresden.de/plip-web/plip/index')
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="file-upload"]').send_keys(ex.PDBfile)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        driver.implicitly_wait(30)
        # confirmation=driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[2]/div/section/div/section/div/section[2]/div/div[2]')
        # print(confirmation.text)
        time.sleep(2)
        name = 'Protein-Ligand Interaction Profiler'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'PLIP' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # SDM: predicts effects of mutation on protein stability
    def SDM(self):
        start = time.time()
        driver.get('http://marid.bioc.cam.ac.uk/sdm2/prediction#')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/form/input[1]').send_keys(ex.PDBfile)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/form/input[3]').send_keys(ex.Mutation_list)
        # predicts reverse mutation
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/form/input[4]').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/div/form/div[2]/div/button').click()
        time.sleep(5)
        name = ' SDM : Predicts Effects of Mutation on Protein Stability'
        inputs = ex.PDBfile + ex.Mutation_list
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'SDM' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # not working : Dynamut Normal mode analysis of 3D protein structures
    def Dynamut_NMS(self):
        start = time.time()
        driver.get("http://biosig.unimelb.edu.au/dynamut/analysis")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "").send_keys(ex.PDBfile)
        # select force fields , C alpha, ANm, pfANM, REACH, sdENM
        if ex.Forcefields == 'ANM':
            driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[1]')
            driver.find_element(By.XPATH,
                                '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[2]/div/div[2]').click()
        elif ex.Forcefields == 'pfANM':
            driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[1]')
            driver.find_element(By.XPATH,
                                '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[2]/div/div[3]').click()
        elif ex.Forcefields == 'REACH':
            driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[1]')
            driver.find_element(By.XPATH,
                                '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[2]/div/div[4]').click()
        elif ex.Forcefields == 'sdenm':
            driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[1]')
            driver.find_element(By.XPATH,
                                '/html/body/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div[2]/div/div[5]').click()
        else:
            pass
        driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/form/div[5]/div/button').click()
        time.sleep(5)
        name = 'DynaMut : Normal Mode Analysis of effect of mutation in protein'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Dynamut' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Single Mutational effect prediction  : prediction of protein stability change upon mutation
    def Dynamut_Smutaion(self):
        start = time.time()
        driver.get('http://biosig.unimelb.edu.au/dynamut/prediction')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="pdb_file"]').send_keys(ex.PDBfile)
        driver.find_element(By.XPATH, '//*[@id="mutation"]').send_keys(ex.Single_mutation)
        driver.find_element(By.XPATH, '//*[@id="chain_single"]').send_keys(ex.Protein_chain)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/form/div[4]/div/button').click()
        time.sleep(5)
        name = 'DynaMut : Single Mutation effect prediction  : prediction of protein stability change upon ' \
               ''
        inputs = ex.PDBfile + ex.Single_mutation
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Dynamut : Single Mutation' + '*' * 50)
        return name, inputs, status, url, ExTime, end

        # Multi Mutational effect prediction  : prediction of protein stability change upon mutation

    # Multi Mutational effect prediction  : prediction of protein stability change upon mutation
    def Dynamut_Mmutaion(self):
        start = time.time()
        driver.get('http://biosig.unimelb.edu.au/dynamut/prediction')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="wild-list"]').send_keys(ex.PDBfile)
        driver.find_element(By.XPATH, '//*[@id="mutation-list"]').send_keys(ex.Mutation_list)
        driver.find_element(By.XPATH, '//*[@id="chain_list"]').send_keys(ex.Protein_chain)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div[4]/div/button').click()
        time.sleep(5)
        name = 'DynaMut : Multi Mutation effect prediction  : prediction of protein stability change upon mutation'
        inputs = ex.PDBfile + ex.Mutation_list
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Dynamut : Multi Mutation' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # CRYSTALP2 - predictor of protein crystallization propensity
    def CrystalP2(self):
        start = time.time()
        driver.get('http://biomine.cs.vcu.edu/servers/CRYSTALP2/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/textarea').send_keys(ex.Fasta)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/input[4]').send_keys(ex.Email)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/input[5]').click()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[1])
        name = 'Crystal P2 : Predictor For Protein Crystallization propensity'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        driver.switch_to.window(driver.window_handles[0])
        end = time.time() - start
        print('*' * 50 + 'CrystalP2' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Deeprefiner high accuracy protein structure refinement by deep network calibration
    def Deeprefiner(self):
        start = time.time()
        driver.get('http://watson.cse.eng.auburn.edu/DeepRefiner/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="inJob"]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '//*[@id="pdbField"]').send_keys(ex.PDBfile)
        driver.find_element(By.XPATH, '//*[@id="submitBtn"]').click()
        time.sleep(4)
        name = 'Deep Refiner High accuracy protein structure refinement'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Deep Refiner' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # QuickGO: Gene Ontology and Gene Annotation
    def Quickgo(self):
        start = time.time()
        driver.get('https://www.ebi.ac.uk/QuickGO/')
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'div.typeaheadsearch > form:nth-child(1) > megasearch:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(
            ex.AlphaFold_input)
        driver.find_element(By.CSS_SELECTOR, 'form.ng-dirty > megasearch:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)').click()
        time.sleep(3)
        confirmation = driver.find_element(By.CSS_SELECTOR, '.quickgo-panel').click()
        time.sleep(1)
        name = 'QuickGO : Gene Ontology and Gene Annotation'
        inputs = ex.AlphaFold_input
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'QuickGO' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # PDBeFold : pairwise comparison and 3D alignment of protein structure
    def PDBeFold(self):
        start = time.time()
        driver.get('https://www.ebi.ac.uk/msd-srv/ssm/cgi-bin/ssmserver')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div[2]/div/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[1]/input').send_keys(
            ex.PDBfile)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div[2]/div/table/tbody/tr/td/form/table[3]/tbody/tr/td/input[2]').click()
        time.sleep(8)
        name = 'PDBeFold'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'PDBeFold' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # PDBsum pictorial database of 3D structures in Protein Data Bank
    def PDBsum(self):
        start = time.time()
        driver.get('https://www.ebi.ac.uk/thornton-srv/databases/cgi-bin/pdbsum/GetPage.pl?pdbcode=index.html')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/table[1]/tbody/tr/td[3]/div[3]/div/div/form/textarea').send_keys(
            ex.Fasta)
        driver.find_element(By.XPATH, '/html/body/div[2]/table[1]/tbody/tr/td[3]/div[3]/div/div/form/input').click()
        time.sleep(5)
        name = 'PDBsum pictorial database of 3D structures in Protein Data Bank'
        inputs = ex.Fasta
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'PDBsum' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Profun : Predicting protein function from 3d structure
    def Profun(self):
        start = time.time()
        driver.get('https://www.ebi.ac.uk/thornton-srv/databases/profunc/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/table[1]/tbody/tr/td[3]/div[2]/div/div/form/input[3]').send_keys(
            ex.PDBfile)
        driver.find_element(By.XPATH, '/html/body/div[2]/table[1]/tbody/tr/td[3]/div[2]/div/div/form/input[4]').click()
        time.sleep(5)
        driver.find_element(By.XPATH,
                            '/html/body/div[4]/table[1]/tbody/tr/td[3]/form/div/div/div/table/tbody/tr[1]/td[3]/input').send_keys(
            ex.Job_name)
        driver.find_element(By.XPATH, '').send_keys('IISER-Tirupati')
        driver.find_element(By.XPATH,
                            '/html/body/div[4]/table[1]/tbody/tr/td[3]/form/div/div/div/table/tbody/tr[5]/td[3]/input').send_keys(
            ex.Email)
        driver.find_element(By.XPATH,
                            '/html/body/div[4]/table[1]/tbody/tr/td[3]/form/div/div/div/table/tbody/tr[9]/td[2]/input').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '//*[@id="contentsarea"]')
        with open('profun.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Profun : Predicting protein function from 3d structure'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Profun' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # RaptorX: [ Not Working ] : Distance based Protein Folding predictions
    def RaptorX(self):
        start = time.time()
        driver.get('http://raptorx.uchicago.edu/ContactMap/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="id_jobname"]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '//*[@id="id_email"]').send_keys(ex.Email)
        driver.find_element(By.XPATH, '//*[@id="id_sequences"]').send_keys(ex.Fasta)
        driver.find_element(By.XPATH, '//*[@id="id_No3DModels"]').click()
        driver.find_element(By.XPATH, '//*[@id="seqInput"]').click()
        time.sleep(4)
        name = 'RaptorX : Distance based Protein Folding predictions'
        inputs = ex.Fasta
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'RaptorX' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # trRosetta : Protein structure prediction by transform restrained rosetta
    def TrRosseta(self):
        start = time.time()
        driver.get('https://yanglab.nankai.edu.cn/trRosetta/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="PDB"]').send_keys(ex.Fasta)
        driver.find_element(By.XPATH, '/html/body/div/fieldset/form/input[3]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '/html/body')
        with open('TrRosseta.text', 'w') as f:
            f.write(confirmation.text)
        name = 'trRosetta : Protein structure prediction by transform restrained rosetta'
        inputs = ex.Fasta
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'trRosetta' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Sequence Analysis, SAS : Sequence Annotated by Structure
    def SAS(self):
        start = time.time()
        driver.get('https://www.ebi.ac.uk/thornton-srv/databases/sas/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/table[1]/tbody/tr/td[3]/form/div[3]/div/div/table/tbody/tr[1]/td[2]/textarea').send_keys(
            ex.Fasta)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/table[1]/tbody/tr/td[3]/form/div[3]/div/div/table/tbody/tr[3]/td/input').click()
        time.sleep(6)
        name = 'SAS : sequence annotated by structure'
        inputs = ex.Fasta
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'SAS' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # The IntFOLD Integrated Protein Structure and Function Prediction Server(Version 6.0)
    def IntFold(self):
        start = time.time()
        driver.get('https://www.reading.ac.uk/bioinf/IntFOLD/IntFOLD6_form.html')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/textarea').send_keys(
            ex.Protein_Sequence)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/input[1]').send_keys(
            ex.AlphaFold_input)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/input[4]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '//*[@id="centerColumn"]')
        with open('IntFOLD.text', 'w') as f:
            f.write(confirmation.text)
        name = 'IntFOLD Integrated Protein Structure and Function Prediction Server'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'IntFOLD' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # DeepGO Web : Protein Function Prediction webserver
    def DeepGO(self):
        start = time.time()
        driver.get('https://deepgo.cbrc.kaust.edu.sa/deepgo/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="id_data"]').send_keys(ex.Fasta)
        driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div/form/button').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]')
        with open('DeepGO.text', 'w') as f:
            f.write(confirmation.text)
        name = 'DeepGO Web : Protein Function Prediction webserver'
        inputs = ex.Fasta
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'DeepGO web' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # ModWeb : A server for protein structure modelling
    def Modweb(self):
        start = time.time()
        driver.get('https://modbase.compbio.ucsf.edu/modweb/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[5]/div[2]/div/div/form/table/tbody/tr[4]/td[2]/input').send_keys(
            ex.Modeller_licence_keys)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[5]/div[2]/div/div/form/table/tbody/tr[5]/td[2]/input').send_keys(
            ex.Job_name)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[5]/div[2]/div/div/form/table/tbody/tr[8]/td[2]/textarea').send_keys(
            ex.Protein_Sequence)
        driver.find_element(By.XPATH,
                            '/html/body/div/div[5]/div[2]/div/div/form/table/tbody/tr[10]/td/center/input[1]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '//*[@id="resulttable"]')
        with open('modweb.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Mod-Web : Protein Structure Modelling'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Modweb' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Consurf structure and Function prediction
    def Consurf_Structure(self):
        start = time.time()
        driver.get('https://consurf.tau.ac.il/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/label/input').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[2]/div[2]/label/input').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/div[1]/div[2]/label/input').click()
        driver.find_element(By.XPATH, '//*[@id="fasta_field"]').send_keys(ex.Fasta)
        driver.find_element(By.XPATH, '//*[@id="auto_select"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="qtitle"]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[6]/div[8]/input').send_keys(ex.Email)
        time.sleep(1)
        Submit = driver.find_element(By.CSS_SELECTOR, "#General_fields > input:nth-child(14)")
        Submit.click()
        time.sleep(5)
        confirmation = driver.find_element(By.XPATH, '//*[@id="maincontentcontainer"]')
        with open('Consurf_Structure.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Consurf Structure Prediction '
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Consurf Structure Prediction' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # IUPRED3 : Prediction of Intrinsically Unstructured Proteins
    def Iupred3(self):
        start = time.time()
        driver.get('https://iupred3.elte.hu/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="inp_seq"]').send_keys(ex.Protein_Sequence)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/form/div[5]/button').click()
        time.sleep(4)
        # confirmation = driver.find_element(By.XPATH,
        #                                    '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div[2]')
        # f = Image.open('Iupred3.png', 'w') as f:
        #     f.write(confirmation.screenshot_as_png)
        name = 'IUPRED3 : Prediction of Intrinsically Unstructured Proteins'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'IUPRED 3' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Muscle : MUltiple Sequence Comparison by Log- Expectation
    def Muscle(self):
        start = time.time()
        driver.get('https://www.ebi.ac.uk/Tools/msa/muscle/')
        driver.implicitly_wait(10)
        msfile = open(ex.MSfile, 'rt')
        k = msfile.read()
        driver.find_element(By.XPATH, '//*[@id="sequence"]').send_keys(k.strip('\n'))
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/section/div/div/form/div[3]/fieldset/div[3]/input').send_keys(Keys.ENTER)
        time.sleep(10)
        confirmation = driver.find_element(By.XPATH, '//*[@id="leftandmaincontent"]')
        with open('Muscle.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Muscle : Multiple Sequence Comparison by Log- Expectation'
        inputs = ex.MSfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Muscle' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # PreDBA : predicts Protein DNA binding affinity using ML
    def PreDBA(self):
        start = time.time()
        driver.get('http://predba.denglab.org/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(ex.ProteinDNA_complex)
        driver.find_element(By.XPATH, '//*[@id="title"]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/fieldset/div[2]/form/div/p[5]/input[2]').click()
        time.sleep(4)
        # confirmation = driver.find_element(By.XPATH, '')
        # with open('', 'w') as f:
        #     f.write(confirmation.text)
        name = 'PreDBA : Predicts Protein DNA binding Affinity using ML'
        inputs = ex.ProteinDNA_complex
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'PreDBA' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Probis : Binding Sites Predictions using structural details
    def Probis(self):
        start = time.time()
        driver.get('https://probis.nih.gov/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div[2]/div/div/form/div[1]/div[3]/span/span[1]/span').click()
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div[2]/div/div/form/div[1]/div[2]/span[1]/span[2]/input').send_keys(
            ex.PDBfile)
        driver.find_element(By.XPATH, '//*[@id="chain_id1"]').send_keys(ex.Protein_chain)
        driver.find_element(By.XPATH, '//*[@id="submit-button"]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div')
        with open('Probis.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Probis : Binding Sites Predictions using structural details'
        inputs = ex.PDBfile + ex.Mutation_list
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Probis' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # eFseek: Protein Function Prediction from structure
    def eFseek(self):
        start = time.time()
        driver.get('https://pdbj.org/eF-seek/top.do')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div/div[7]/form/table/tbody/tr[2]/td[2]/input').send_keys(
            ex.PDBfile)
        driver.find_element(By.XPATH, '/html/body/div/div/div[7]/form/table/tbody/tr[4]/td[2]/input').send_keys(
            ex.Job_name)
        driver.find_element(By.XPATH, '/html/body/div/div/div[7]/form/table/tbody/tr[3]/td[2]/input').send_keys(
            ex.Email)
        driver.find_element(By.XPATH, '/html/body/div/div/div[7]/form/table/tbody/tr[9]/td/input').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[1]/td[2]')
        with open('eFseek', 'w') as f:
            f.write(confirmation.text)
        name = 'eFseek : Protein Function Prediction from structure'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'eFseek' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # incomplete # servers down
    # SuMo : ligand binding sites matching your protein structure or inversely, for finding protein structures matching a given site in your protein
    def SuMo(self):
        start = time.time()
        driver.get('http://sumo-pbil.ibcp.fr/cgi-bin/sumo-welcome')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/form/p[1]/input[2]').send_keys(ex.PDBfile)
        driver.find_element(By.XPATH, '/html/body/form/p[2]/input[2]').click()
        # driver.find_element(By.XPATH, '')
        # driver.find_element(By.XPATH, '')
        # driver.find_element(By.XPATH, '')
        # time.sleep(4)
        # confirmation = driver.find_element(By.XPATH, '')
        # with open('', 'w') as f:
        #     f.write(confirmation.text)
        name = 'SuMo : ligand binding sites matching your protein structure '
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'SuMo' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # 3D Ligand Site : Protein Ligand binding site predictions
    def LigandSite(self):
        start = time.time()
        driver.get('https://www.wass-michaelislab.org/3dlig/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '//*[@id="jobname"]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '//*[@id="seq1"]').send_keys(ex.Protein_Sequence)
        driver.find_element(By.XPATH, '/html/body/aside/div[1]/form/button').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '/html/body')
        with open('Ligandsite.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Ligandsite : : Protein Ligand binding site predictions'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'LigandSite' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # FunFold2 Protein Binding site Prediction server
    def FunFold2(self):
        start = time.time()
        driver.get('https://www.reading.ac.uk/bioinf/FunFOLD/FunFOLD_form_2_0.html')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/p[2]/textarea').send_keys(
            ex.Protein_Sequence)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/p[2]/input[2]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/p[2]/input[5]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '//*[@id="centerColumn"]')
        with open('Funfold3.text', 'w') as f:
            f.write(confirmation.text)
        name = 'FunFold2 Protein Binding site Prediction server'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Funfold2' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Mcoffee : Aligns Proteins By combining output of popular aligners
    def Mcofee(self):
        start = time.time()
        driver.get('https://tcoffee.crg.eu/apps/tcoffee/do:mcoffee')
        driver.implicitly_wait(10)
        msfile = open(ex.MSfile, 'r')
        driver.find_element(By.XPATH, '//*[@id="seqs"]').send_keys(msfile.read())
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '/html/body/div[3]/div/table/tbody/tr[2]/td[2]')
        with open('Mcoffe.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Mcoffee : Aligns Proteins By combining output of popular aligners'
        inputs = ex.MSfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Mcoffee' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # Expresso aligns protein sequences using structural information
    def Expresso(self):
        start = time.time()
        driver.get('https://tcoffee.crg.eu/apps/tcoffee/do:expresso')
        driver.implicitly_wait(10)
        msfile = open(ex.MSfile, 'r')
        driver.find_element(By.XPATH, '//*[@id="seqs"]').send_keys(msfile.read())
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '/html/body/div[3]/div/table/tbody/tr[2]/td[2]')
        with open('Expresso.text', 'w') as f:
            f.write(confirmation.text)
        name = 'Expresso aligns Protein Squences using structural information'
        inputs = ex.MSfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Expresso' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # nFOLD3 : Protein Fold Recognition Server
    def nFOLD3(self):
        start = time.time()
        driver.get('https://www.reading.ac.uk/bioinf/nFOLD/nFOLD_form.html')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/b/form/p[2]/textarea').send_keys(
            ex.Protein_Sequence)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/b/form/p[2]/input[2]').send_keys(
            ex.AlphaFold_input)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/b/form/p[2]/input[3]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '//*[@id="centerColumn"]')
        with open('nFOLD3.text', 'w') as f:
            f.write(confirmation.text)
        name = 'nFOLD3 : Protein Fold Recognition Server'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'nFOLD3' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # ModFOLD : Model Quality Assessment Server
    def ModFOLD(self):
        start = time.time()
        driver.get('https://www.reading.ac.uk/bioinf/ModFOLD/ModFOLD8_form.html')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/p[2]/textarea').send_keys(
            ex.Protein_Sequence)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/p[2]/input[8]').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/form/p[2]/input[10]').click()
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '//*[@id="centerColumn"]')
        with open('ModFOLD.text', 'w') as f:
            f.write(confirmation.text)
        name = 'ModFOLD : Model Quality Assessment Server'
        inputs = ex.Protein_Sequence
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'ModFOLD' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # MAFFT : Multiple alignment program for amino acid or nucleotide sequences
    def MAFFT(self):
        start = time.time()
        driver.get('https://mafft.cbrc.jp/alignment/server/')
        driver.implicitly_wait(10)
        msfile = open(ex.MSfile, 'rt')
        k = msfile.read()
        driver.find_element(By.XPATH, '/html/body/div[2]/form/div/div[1]/textarea').send_keys(k.strip('\n'))
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[2]/form/div/div[2]/p[14]/input').send_keys(ex.Job_name)
        driver.find_element(By.XPATH, '//*[@id="dashstr"]').click()
        driver.find_element(By.XPATH, '//*[@id="anysymbol"]').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/form/div/p[6]/input[1]').click()
        time.sleep(4)
        name = 'MAFFT : Multiple alignment program for amino acid or nucleotide sequences'
        inputs = ex.MSfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'MAFFT' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    # K align : Multiple sequence Alignment program
    def Kalign(self):
        start = time.time()
        driver.get('https://msa.sbc.su.se/cgi-bin/msa.cgi')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div[3]/p[2]/a[1]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[3]/input').send_keys(ex.MSfile)
        driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[8]/input').click()
        time.sleep(4)
        # confirmation = driver.find_element(By.XPATH, '/html/body')
        # with open('Kalign.png', 'w') as f:
        #     f.write(confirmation.screenshot_as_png)
        name = 'K align : Multiple sequence Alignment program'
        inputs = ex.MSfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'K Alignment' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    def h(self):
        start = time.time()
        driver.get('')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '')
        with open('', 'w') as f:
            f.write(confirmation.text)
        name = '[]'
        inputs = ex.PDBfile + ex.Mutation_list
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + '[]' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    def h(self):
        start = time.time()
        driver.get('')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        driver.find_element(By.XPATH, '')
        time.sleep(4)
        confirmation = driver.find_element(By.XPATH, '')
        with open('', 'w') as f:
            f.write(confirmation.text)
        name = '[]'
        inputs = ex.PDBfile + ex.Mutation_list
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + '[]' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    def NGL(self):
        start = time.time()
        driver.get('https://nglviewer.org/ngl/?script=showcase/ferredoxin')
        driver.implicitly_wait(10)
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/input').send_keys(ex.PDBfile)
        time.sleep(4)
        name = 'NGL Viewer'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'NGL' + '*' * 50)
        return name, inputs, status, url, ExTime, end

    def Mol(self):
        start = time.time()
        driver.get('https://molstar.org/viewer/')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div[4]/div/button').click()
        time.sleep(2)
        # driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div[4]/div[2]').click()
        # time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/input').send_keys(ex.PDBfile)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div[4]/div[5]/div/button').click()
        time.sleep(4)
        name = 'Mol Visualiser'
        inputs = ex.PDBfile
        status = 'Submitted'
        url = driver.current_url
        ExTime = time.ctime()
        end = time.time() - start
        print('*' * 50 + 'Mol' + '*' * 50)
        return name, inputs, status, url, ExTime, end
    def clear_it(self):
        driver.delete_cookie()
        driver.localStorage.clear()
        driver.sessionStorage.clear()

def run(seq, user_input):
    wb = Workbook()
    sh = wb.active
    sh.title = "PMToolkit-Sequence Report"
    sh.append(["Tool-Name", "User-Input", "Job-Status", "Result URL", "Execution-Time", "Top Hits"])

    # submit the jobs
    for idx, tool in enumerate(user_input):
        if tool == "ITASSER":
            name, inputs, st, url, ExTime, end = seq.ITASSER()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "AlphaFold":
            name, inputs, st, url, ExTime, end = seq.AlphaFold()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "serp":
            name, inputs, st, url, ExTime, end = seq.serp()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "reactome":
            name, inputs, st, url, ExTime, end = seq.reactome()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "CoeViz2":
            name, inputs, st, url, ExTime, end = seq.CoeViz2()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "flDPnn":
            name, inputs, st, url, ExTime, end = seq.flDPnn()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "interpro":
            name, inputs, st, url, ExTime, end = seq.interpro()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "SDM":
            name, inputs, st, url, ExTime, end = seq.SDM()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "PLIP":
            name, inputs, st, url, ExTime, end = seq.PLIP()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "mTMalign":
            name, inputs, st, url, ExTime, end = seq.mTMalign()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "ProteinContactAtlas":
            name, inputs, st, url, ExTime, end = seq.ProteinContactAtlas()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "PDBflex":
            name, inputs, st, url, ExTime, end = seq.PDBflex()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "iCn3D":
            name, inputs, st, url, ExTime, end = seq.iCn3D()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "xtal_pred":
            name, inputs, st, url, ExTime, end = seq.xtal_pred()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "P2RANK":
            name, inputs, st, url, ExTime, end = seq.P2RANK()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "fPocket":
            name, inputs, st, url, ExTime, end = seq.fPocket()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "swiss":
            name, inputs, st, url, ExTime, end = seq.swiss()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "Dynamut_NMS":
            name, inputs, st, url, ExTime, end = seq.swiss()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Dynamut_Smutaion":
            name, inputs, st, url, ExTime, end = seq.Dynamut_NMS()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Dynamut_Mmutaion":
            name, inputs, st, url, ExTime, end = seq.Dynamut_Mmutaion()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "CrystalP2":
            name, inputs, st, url, ExTime, end = seq.CrystalP2()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Deeprefiner":
            name, inputs, st, url, ExTime, end = seq.Deeprefiner()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "PDBefold":
            name, inputs, st, url, ExTime, end = seq.PDBeFold()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "PDBsum":
            name, inputs, st, url, ExTime, end = seq.PDBsum()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "RaptorX":
            name, inputs, st, url, ExTime, end = seq.RaptorX()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "TrRosseta":
            name, inputs, st, url, ExTime, end = seq.TrRosseta()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "SAS":
            name, inputs, st, url, ExTime, end = seq.SAS()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "IntFold":
            name, inputs, st, url, ExTime, end = seq.IntFold()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "DeepGO":
            name, inputs, st, url, ExTime, end = seq.DeepGO()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Modweb":
            name, inputs, st, url, ExTime, end = seq.Modweb()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Consurf_Structure":
            name, inputs, st, url, ExTime, end = seq.Consurf_Structure()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        # elif tool == "Consurf":
        #     name, inputs, st, url, ExTime, end = seq.Consurf()
        #     sh.append([name, inputs, st, url, ExTime])
        #     end_time.append(end)

            # style work book
        elif tool == "Iupred3":
            name, inputs, st, url, ExTime, end = seq.Iupred3()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Muscle":
            name, inputs, st, url, ExTime, end = seq.Muscle()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "PreDBA":
            name, inputs, st, url, ExTime, end = seq.PreDBA()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Probis":
            name, inputs, st, url, ExTime, end = seq.Probis()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "eFseek":
            name, inputs, st, url, ExTime, end = seq.eFseek()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "nFOLD3":
            name, inputs, st, url, ExTime, end = seq.nFOLD3()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "ModFOLD":
            name, inputs, st, url, ExTime, end = seq.ModFOLD()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "MAFFT":
            name, inputs, st, url, ExTime, end = seq.MAFFT()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
            # style work book
        elif tool == "Kalign":
            name, inputs, st, url, ExTime, end = seq.Kalign()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "flDPnnM":
            name, inputs, st, url, ExTime, end = seq.flDPnnM()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "flDPnnS":
            name, inputs, st, url, ExTime, end = seq.flDPnnS()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "Quickgo":
            name, inputs, st, url, ExTime, end = seq.Quickgo()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "Profun":
            name, inputs, st, url, ExTime, end = seq.Profun()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "LigandSite":
            name, inputs, st, url, ExTime, end = seq.LigandSite()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "FunFold2":
            name, inputs, st, url, ExTime, end = seq.FunFold2()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "Mcofee":
            name, inputs, st, url, ExTime, end = seq.Mcofee()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)
        elif tool == "Expresso":
            name, inputs, st, url, ExTime, end = seq.Expresso()
            sh.append([name, inputs, st, url, ExTime])
            end_time.append(end)

        cell1 = sh['A1']
        cell1.font = Font(bold=True, size=14, color="00339966")
        cell2 = sh['B1']
        cell2.font = Font(bold=True, size=14, color="00339966")
        cell3 = sh['C1']
        cell3.font = Font(bold=True, size=14, color="00339966")
        cell4 = sh['D1']
        cell4.font = Font(bold=True, size=14, color="00339966")
        cell5 = sh['E1']
        cell5.font = Font(bold=True, size=14, color="00339966")
        cell6 = sh['F1']
        cell6.font = Font(bold=True, size=14, color="00339966")
        for row in sh:
            for cell in row:
                cell.alignment = Alignment(wrapText=True)
        col_a = sh.column_dimensions['A']
        col_a.width = 20.0
        col_b = sh.column_dimensions['B']
        col_b.width = 15.0
        col_c = sh.column_dimensions['C']
        col_c.width = 15.0
        col_d = sh.column_dimensions['D']
        col_d.width = 50.0
        col_e = sh.column_dimensions['E']
        col_e.width = 25.0
        col_e = sh.column_dimensions['E']
        col_e.width = 25.0
        wb.save("PMToolKit_report.xlsx")


def email_to_client():
    msg = EmailMessage()
    msg['Subject'] = 'PM Toolkit Results Notice!!'
    msg['From'] = 'PM toolkit Developer'
    msg['To'] = ex.Email
    email_template_file_path = r"D:\PMtk\PMtoolkit_email_template.txt"
    excel_file_loc = r'D:\PMtk\PMToolKit_report.xlsx'

    with open(email_template_file_path) as myfile:
        data = myfile.read()
        msg.set_content(data)

    with open(excel_file_loc, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="Report", subtype="xlsx", filename=f.name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(ex.sender, ex.password)
        server.send_message(msg)
    return print('Email sent !!!')


end_time = []
#ex = Example_inputs()
#Seq_obj = Sequence()
#Seq_obj.AlphaFold()
#Seq_obj.Mol()
####################################

# user_input = ["AlphaFold", "serp", "flDPnn", "CoeViz2", "interpro", "ITASSER", "reactome", "swiss"]

# user_input = ["ITASSER", "AlphaFold", "interpro", "flDPnn", "CoeViz2", "serp",  "reactome", "swiss",
#               "PDBflex", "Consurf", "mTMalign", "CUPSAT", "P2RANK", "iCn3D", "ProteinContactAtlas", "PLIP", "SDM",
#               "Dynamut_NMS", "Dynamut_Smutaion", "Dynamut_Mmutaion", "Deeprefiner", "PDBefold", "PDBsum",
#                "TrRosseta", "SAS", "IntFold", "DeepGO", "Modweb", "Consurf_Structure", "Iupred3", "Muscle",
#               "PreDBA", "Probis", "SuMo", "LigandSite", "FunFold2", "Mcofee", "Expresso", "nFOLD3", "ModFOLD",
#               "MAFFT", "Kalign", "Quickgo", "CrystalP2", "RaptorX", "eFseek", "xtal_pred", "Profun]

#
# user_input = ["AlphaFold", "interpro", "CoeViz2",  "reactome", "swiss",
#                "PDBflex",  "TrRosseta", "SAS", "IntFold", "DeepGO", "Modweb", "Consurf_Structure",
#                "Iupred3", "LigandSite", "FunFold2", "Expresso", "nFOLD3", "ModFOLD", "Kalign", "CrystalP2", "xtal_pred"]

#####################################
# # Time Per Method PLot
# #
# mean = np.sum(end_time) / len(end_time)
# print(mean)
# plt.bar(user_input, end_time)
# plt.style.use('ggplot')
# plt.title('Time Taken Per Method', loc='left', fontname='Franklin Gothic Medium', fontsize=18)
# plt.xlabel('Tool Selected')
# plt.xticks(fontsize=8)
# plt.ylabel("Time (seconds)", fontname='Gabriola', fontsize=15)
# plt.figure(facecolor='black', edgecolor='white', dpi=300)
# plt.tight_layout(h_pad=2, w_pad=1)

# run(Seq_obj, user_input)
# email_to_client()
# e
