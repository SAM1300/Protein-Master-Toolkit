# views for website
from typing import List, Union, Any
import matplotlib
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import requests
from html.parser import HTMLParser
from ASSAP import models
import time
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mass_mail
import os

def input(request):
    
    return render(request, "form.html")



def result(request):
    start = time.time()
    if request.method == 'POST':
        job_name = request.POST.get("jobname", "No job name provided")
        email = request.POST.get("email", "No email Provided")
        Q_P = request.POST.get("fname", "No Query Protein Name Provided")
        Q_P_S = request.POST.get("qps-text", "No Query Protein Sequence Provided ")
        DSM = request.POST.get("Mutation Text", "No Single mutation text provided")
        PC = request.POST.get("Protein Chain", "No Protein Chain Provided")
        Forcefields = request.POST.get("Forcefields", "No forcefields provided")
        MLK = request.POST.get("MLK", "No key provided")
        jobid = job_name + "_" + time.ctime()
        data = request.POST.getlist("selectInput")
        file = {}
        Q_P_Sfile = request.FILES['qps-file'] if 'qps-file' in request.FILES else None
        if Q_P_Sfile:
            fs = FileSystemStorage()
            filename = fs.save(Q_P_Sfile.name, Q_P_Sfile)
            u_f_u = fs.url(filename)
            u_f_p = fs.path(filename)
            file['u_f_p'] = u_f_p
            file['u_f_u'] = u_f_u
        DMM = request.FILES['Mutation File'] if 'Mutation File' in request.FILES else None
        MSF = request.FILES['MSF'] if 'MSF' in request.FILES else None
        Mutation_list = request.FILES['Mutation List'] if 'Mutation List' in request.FILES else None
        user_input = ["AlphaFold", "interpro", "CoeViz2", "reactome", "swiss", "PDBflex", "TrRosseta", "SAS", "IntFold",
                      "DeepGO", "Modweb", "Consurf_Structure", "Iupred3", "LigandSite", "FunFold2", "Expresso",
                      "nFOLD3", "ModFOLD", "Kalign", "CrystalP2", "Muscle", "xtal_pred", "ITASSER", "flDPnnS",
                      "flDPnnM", "serp", "mTMalign", "CUPSAT", "P2RANK", "iCn3D", "ProteinContactAtlas", "SDM_Single",
                      "PLIP", "SDM_Multi", "Dynamut_NMS", "Phyre", "Dynamut_Smutaion", "Dynamut_Mmutaion",
                      "Deeprefiner", "Quickgo", "PDBeFold", "PDBsum", "Profun", "Probis", "MAFFT", "Mcofee", "SuMo",
                      "eFseek", "JSMol"]
        inputs = []
        c = 1
        for i in user_input:
            u_i = request.POST.get(i)
            #print(c, u_i)
            if (u_i != None):
                print(u_i)
                inputs.append(u_i)
        
     
        user = User.objects.create_user(jobid, email)
        user.save()
        login(request, user)
        inst = models.result_model(jobid=jobid, user=request.user, jobname=job_name, Q_P=Q_P, Q_P_S=Q_P_S,
                                   PDB=Q_P_Sfile,
                                   DSM=DSM, DMM=DMM, MSF=MSF, PC=PC, Forcefield=Forcefields, List=Mutation_list,
                                   MLK=MLK)
        inst.save()
        ins = list(models.result_model.objects.filter(
            jobid=models.result_model.objects.all()[len(models.result_model.objects.all()) - 1].jobid))

        def Merge(dict1, dict2):
            return (dict2.update(dict1))

        import sys
        sys.path.insert(0, '/../PMtk-20220215T094451Z-001/PMtk')
        from PMTK import Sequence
        seq = Sequence()
        # seq.clear_it()
        # seq.Consurf_Structure()
        methods = []
        url = {}
        for i in range(len(inputs)):
            for j in range(len(user_input)):
                if (inputs[i] == user_input[j]):
                    print(type(inputs[i]))
                    methods.insert(i, "seq." + inputs[i] + "()")

        # url = [Sequence().AlphaFold()[3], Sequence().flDPnnS()[3], Sequence().CoeViz2()[3], Sequence().reactome()[3], Sequence.]
        Ext = 0
        Ext_dict = {}
        for i in range(len(inputs)):
            print("Check 1")
            link = eval(methods[i])[3]
            ex = eval(methods[i])[5]
            if inputs[i] == "nFOLD3" or inputs[i] == "Iupred3" or inputs[i] == "mTMalign" or inputs[i] == "Modweb" or \
                    inputs[i] == "ModFOLD" or inputs[i] == "LigandSite":
                url[methods[i]] = []
            if inputs[i] != "mTMalign":
                url[methods[i]].append("/static/Html/" + inputs[i] + jobid + ".png")
            if inputs[i] == "mTMalign":
                link = "/static/Html/mTMalign" + jobid + ".html"
                url[methods[i]].append(link)
            else:
                url[methods[i]] = link
        Ext_dict[inputs[i]] = ex
        Ext = Ext + ex

        # print(Ext_dict)
        pmc = f"https://www.ebi.ac.uk/europepmc/webservices/rest/searchPOST?query={Q_P}%20sort_date:y&format=json&pageSize=10&resultType=core"
        r_pmc = requests.post(pmc, headers={"Content-type": "application/x-www-form-urlencoded"})
        data_pmc = r_pmc.json()

        plos = f'http://api.plos.org/search?q=title:{Q_P} and body:{Q_P}&fl=id,abstract,title,author&wt=json'
        r_plos = requests.post(plos, headers={"Content-type": "application/json"})
        data_plos = r_plos.json()

        # list = os.listdir("")

        # crossref = f"http://api.crossref.org/works?query={Q_P}&sample=10"
        # r_cross = requests.post(crossref, headers={"Content-type": "application/json"})
        # data_cross = r_cross.text()
        # print(data_cross)
        # mol = seq.NGL()[3]
        # ins = list(models.result_model.objects.filter(jobid=result_model.objects.all()[len(result_model.objects.all()) - 1].jobid))
        params = {"jobname": job_name, "email": email, "Q_P_N": Q_P, "inputs": inputs, "url": url, "Exttime": Ext,
                  "Q_P_S": Q_P_S, 'data_pmc': data_pmc['resultList']['result'],
                  "res_plos": data_plos['response']['docs']}
        Merge(file, params)
        # print(u_f_p)

        # r = requests.post("https://europepmc.org/RestfulWebService")
        # print(r.json())
        # arr = {"Structure Prediction": ["Alphafold","Consurf Server", "Orion Web Server", "Lzerd Server", "I-Tasser"],a
        #  "Gene Ontology and Functional Analysis" : ["Inter-Pro","Deep-GO"],

        #  }
        ins = list(models.result_model.objects.filter(
            jobid=models.result_model.objects.all()[len(models.result_model.objects.all()) - 1].jobid))
        print(ins[len(ins) - 1].jobname)
        end = time.time()
        print("Execution Time:", end - start)

        if data[0] == "PDB Data":
            print("PDB DAta")
            return render(request, "logo.html", params)
        if data[0] == "Sequence Data":
            print("Sequebce Data")
            return render(request, "Sequence.html", params)
        if data[0] == "Sequence and PDB Data":
            print("Seq and pdb")
            return render(request, "SequencePDB.html", params)
        else:
            return HttpResponse("Error-404")
print(result)


def contact(request):
    F_N = request.POST.get("Name", "No name Provided")
    Email = request.POST.get("Email", "No email provided")
    msg = request.POST.get("Message", "No message provided")
    sub = request.POST.get("sub", "Not clicked")
    if F_N != "No name Provided" and Email != "No email provided" and msg != "No message provided":
        print("entered loop")
        subject = "Feedback for ASSAP 1.0"
        sub_new = "Acknowledgement for using ASSAP 1.0"
        msg_new = "Thanks for giving feedback. We will revert back to you soon."
        message = f"Hi, this is {F_N}." + "\n" + msg + "\n" + f"My email id is:{Email}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        reci_list = [Email]
        datatuple = ((subject, message, email_from, recipient_list), (sub_new, msg_new, email_from, reci_list))
        send_mass_mail(datatuple)
    if sub != "Not clicked":
        messages.success(request, "Thanks for your feedback. We will get back to you soon.")
        return redirect("contacts")

    return render(request, "Contact.html")


def about(request):
    return render(request, "About.html")
