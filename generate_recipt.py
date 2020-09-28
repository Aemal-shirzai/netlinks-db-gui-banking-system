import os
import sys 
import subprocess
from datetime import datetime
import fpdf
from authentication import current_user
from functions import number_format

class Recipt:
    """This class contains methods for generating recipts.

    Public Methods:
    --------------
    balnace_reciept(): -- It generate a receipt for checking balance. 
        and call the open_file() functioin to directly open the generated pdf
        reciept.
    deposit_reciept: It generate a receipt for depositing to balance. 
        and call the open_file() functioin to directly open the generated pdf
        reciept.
    withdraw_reciept: It generate a receipt for withdrawing  balance. 
        and call the open_file() functioin to directly open the generated pdf
        reciept.
    """

    @staticmethod
    def deposit_reciept(new_amount, depsoited_amount):
        """This function create a recipt bill for deposit balance and open the
         file.
         
         parameters: 
         new_amount: the amount of money after depsoit
         deposited_amount: the amount of desposited money
         """
        
        id = current_user().id
        name = current_user().name
        new_amount = number_format(new_amount)
        depsoited_amount = number_format(depsoited_amount)

        recipt = fpdf.FPDF('P', 'mm', (115,115))
        recipt.add_page()
        recipt.set_font('Arial', '', 9)

        text1 = "Welcome To Banking System".center(75,"-")
        text2 = f"User ID: {id} \n Name: {name} \n Date: {datetime.now()} \n"
        text3 = f"Desposit Money \n"
        text4 = f"Deposited Amount: {depsoited_amount} Afg \n"
        text5 = f"New Balance: {new_amount} Afg\n"
        text6 = "Thank You".center(80,"-")
        text= f"{text1} \n {text2} {text3} {text4} {text5} {text6}"

        recipt.multi_cell(100, 10, text, border=0, align='c')
        recipt.output(f"{id}{name}-recipt.pdf")

        #open the recipt file
        run_file(f"{id}{name}-recipt.pdf")


    @staticmethod
    def withdraw_reciept(new_amount, withdrawed_amount):
        """This function create a recipt bill for withdraw balance and open the
        file.
        
        parameters: 
        new_amount: the amount of money after depsoit
        withdrawd_amount: the amount of desposited money
        """
    
        id = current_user().id
        name = current_user().name
        new_amount = number_format(new_amount)
        withdrawed_amount = number_format(withdrawed_amount)

        recipt = fpdf.FPDF('P', 'mm', (115,115))
        recipt.add_page()
        recipt.set_font('Arial', '', 9)

        text1 = "Welcome To Banking System".center(75,"-")
        text2 = f"User ID: {id} \n Name: {name} \n Date: {datetime.now()} \n"
        text3 = f"Withdraw Money \n"
        text4 = f"Withdrawed Amount: {withdrawed_amount} Afg \n"
        text5 = f"New Balance: {new_amount} Afg\n"
        text6 = "Thank You".center(80,"-")
        text= f"{text1} \n {text2} {text3} {text4} {text5} {text6}"

        recipt.multi_cell(100, 10, text, border=0, align='c')
        recipt.output(f"{id}{name}-recipt.pdf")

        #open the recipt file
        run_file(f"{id}{name}-recipt.pdf")


    @staticmethod
    def balance_reciept():
        """This function create a recipt bill for checking balance and open the
         file"""

        id = current_user().id
        name = current_user().name
        balance = number_format(current_user().balance)
        recipt = fpdf.FPDF('P', 'mm', (115,110))
        recipt.add_page()
        recipt.set_font('Arial', '', 9)

        text1 = "Welcome To Banking System".center(75,"-")
        text2 = f"User ID: {id} \n User Name: {name} \n Date: {datetime.now()}\n"
        text3 = f"Check Balnace \n Amount: {balance} AFG \n"
        text4 = "Thank You".center(80,"-")
        text= f"{text1} \n {text2} {text3} {text4}"

        recipt.multi_cell(100, 10, text, border=0, align='c')
        recipt.output(f"{id}{name}-recipt.pdf")

        #open the recipt file
        run_file(f"{id}{name}-recipt.pdf")


   
def run_file(filename):
    """Open the pdf reciept.

    It checks the operating system and based on the operating system it opens
    the pdf file.
    """
    platform = sys.platform
    if platform == "win32":
        os.startfile(filename)
    elif platform == "darwin":
        subprocess.call(["open", filename])
    else:
        # for linux
        subprocess.call(["xdg-open", filename])