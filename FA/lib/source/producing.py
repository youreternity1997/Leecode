import asyncio # 編寫並發代碼。它提供了協程、事件循環、任務和各種基於異步 I/O 的高級同步原語，幫助你編寫高效的異步程序。
# 協程是一種可以暫停和恢復執行的函數。使用 async def 定義協程函數，並使用 await 關鍵字來等待異步操作完成。
import signal
import psutil
import os
all_env_vars = os.environ
#print('all_env_vars=', all_env_vars)
import os
current_directory = os.getcwd()
#print(f"Current working directory: {current_directory}")
import aiofiles # 異步文件操作
import sys
import subprocess
import json
import gc
# 从您的项目中导入配置加载函数
from dto.produce_dataset_state_manager import LLMProduceDatasetStateManager

import unittest.mock
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = "D:\algorithm\Leecode\FA"

class ProducingProcess:
    def __init__(self,
                 FileFolder,
                 UploadFile,
                 Name,
                 Chosen_Model,
                 num_QandA,
                 NoLimit_QandA,
                 ):
        
        self.FileFolder = FileFolder
        self.UploadFile = UploadFile
        self.Name = Name
        self.Chosen_Model = Chosen_Model
        self.num_QandA = num_QandA
        self.NoLimit_QandA = NoLimit_QandA
        self.chunk_size = 700
        self.chunk_overlap = 300

        self.tokenizer = None
        self.model = None
        self.parser = None
        self.device = None
        
        self.json_dataset_list = []
        self.json_dataset_dict = {}
        self.process = None
        self.process_pid = None
        
        #self.task = None,
        self.conda_env = None

    async def start(self):
        chosen_model=self.Chosen_Model,
        num_qanda=self.num_QandA,
        no_limit_qanda = 'True' if self.NoLimit_QandA else 'False',
        chunk_size=self.chunk_size,
        chunk_overlap=self.chunk_overlap,
        default_llm_model_name=self.default_LLM_model_name

        import shlex
        upload_file_literal   = repr(self.UploadFile)        # 變成 "['/home/xxx', '/home/yyy']"
        safe_upload_file_literal  = shlex.quote(upload_file_literal)
        print("upload_file_literal===", upload_file_literal)
        print("safe_upload_file_literal====", safe_upload_file_literal)

        #export PATH="/opt/miniconda3/bin:$PATH"
        #eval "$(/opt/miniconda3/bin/conda shell.bash hook)"
        commands = f"""
                    #!/bin/bash
                    conda activate {"LLM"}
                    conda info --envs
                    echo $CONDA_DEFAULT_ENV
                    pwd
                    python -c "import json; from lib.source.core.llm_produce_dataset.core_llm_produce_dataset import llm_producing_dataset; llm_producing_dataset(Name='{self.Name}',UploadFile={safe_upload_file_literal}, Chosen_Model='{chosen_model[0]}', num_QandA={num_qanda[0]}, NoLimit_QandA={no_limit_qanda[0]}, chunk_size={chunk_size[0]}, chunk_overlap={chunk_overlap[0]}, default_LLM_model_name='{default_llm_model_name}')"
                    """
        print('commands=', commands)
        try:
            self.process = subprocess.Popen(
                commands,
                shell=True,
                #env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            self.process_pid = self.process.pid
            print(f"Subprocess PID: {self.process_pid}")
        except Exception as e:
            print(f"Error during producing subprocess process: {e}")

        stdout, stderr = self.process.communicate()
        command_content = stdout.decode().strip()
        print('command_content==================================\n', command_content)
        print("STDERR==========================================\n", stderr.decode())
        
        temp_dataset_jsonfile_path = os.path.join(data_dir, self.Name+'.json')
        try:
            os.makedirs(os.path.dirname(temp_dataset_jsonfile_path), exist_ok=True)
            with open(temp_dataset_jsonfile_path, 'r') as json_file:
                dataset_data = json.load(json_file)
        except FileNotFoundError:
            print(f"File not found: {temp_dataset_jsonfile_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        print('------------------------------------produce.py end')
        return dataset_data

        # except Exception as e:
        #     print(f"Error during producing process: {e}")


    async def stop(self):
        print("stopping producing...")
        self.json_dataset_list = []
        self.json_dataset_dict = {}

        if self.process:
            try:
                # 發送 SIGTERM 信號
                self.process.terminate()
                # 異步等待進程結束
                self.process.wait()
                print(f"Producing process stopped with exit code {self.process.returncode}")
                kill_proc_tree(self.process.pid)
                # 终止进程
                os.kill(self.process.pid, signal.SIGTERM)

            except Exception as e:
                try:
                    self.process.kill()
                    self.process.wait()
                    print(f"Producing process forcefully stopped with exit code {self.process.returncode} - {e}")
                except Exception as e:
                    print(f"Error forcefully stopping the producing process: {e}")


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    if including_parent:
        parent.kill()


def load_file_data(File, Filename):
    from llama_index.core import Settings, SimpleDirectoryReader
    from llama_index.core.node_parser import JSONNodeParser
    from llama_index.readers.file import (
        DocxReader,
        PDFReader,
        FlatReader,
        CSVReader,
    )
    # if '~/' in UploadFile:
    #     UploadFile = UploadFile.replace('~/', '')
    #     UploadFile = os.path.join(home_directory, UploadFile)

    if Filename.endswith('.json'):
        try:
            json_string = SimpleDirectoryReader(input_files=[File],  filename_as_id=True).load_data()
            return json_string
        except json.JSONDecodeError as e:
            print(f"Error: The format of json is wrong. Please rewrite the wrong json format into the correct one. (Error decoding JSON: {e})") #print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Error: Can't open the import Json file with all methods! (An unexpected error occurred: {e})")

    elif Filename.endswith('.txt'):
        parser = FlatReader()
        file_extractor = {".txt": parser}
        try:
            txt_string = SimpleDirectoryReader(input_files=[File], file_extractor=file_extractor).load_data()
            return txt_string
        except Exception as e:
            print(f"Error: Can't open the import txt file with all methods! (An unexpected error occurred: {e})")
    
    elif Filename.endswith('.docx'):
        parser = DocxReader()
        file_extractor = {".docx": parser}
        try:
            doc_string = SimpleDirectoryReader(input_files=[File], file_extractor=file_extractor).load_data()
            return doc_string
        except Exception as e:
            print(f"Error: Can't open the import Word file with all methods! (An unexpected error occurred: {e})")

    elif Filename.endswith('.pdf'):
        parser = PDFReader()
        file_extractor = {".pdf": parser}
        try:
            pdf_string = SimpleDirectoryReader(input_files=[File], file_extractor=file_extractor).load_data()
            return pdf_string
        except Exception as e:
            print(f"Error: Can't open the import PDF file with all methods! (An unexpected error occurred: {e})")

    elif Filename.endswith('.csv') or Filename.endswith('.xlsx'):
        parser = CSVReader() # PandasCSVReader()
        file_extractor = {".csv": parser}
        try:
            csv_string = SimpleDirectoryReader(input_files=[File], file_extractor=file_extractor).load_data()
            return csv_string     
        except Exception as e:
            print(f"Error: Can't open the import CSV file with all methods! (An unexpected error occurred: {e})")
    
    return None


def QA_from_response(response, json_dataset_list, json_dataset_dict, repeat_num, question_identifiers, ans_identifiers, ans_end_identifiers):
    try:
        Each_QA_list = response.split('\n\n')
        for QA in Each_QA_list:
            Question = ''
            Answer = ''
            Q_begin_index = 0
            A_begin_index = 0
            Q_end_index = 1
            A_end_index = 1
            if ('(Question: and Answer: )'in QA) or ('（問題：和答案：）'in QA) or ('（问题：和答案：）'in QA):
                continue

            for identifier in question_identifiers:
                if identifier in QA:
                    if identifier in ['What', 'How', 'Where', 'When', 'Who', 'which']:
                        Q_begin_index = QA.find(identifier)
                    else:
                        Q_begin_index = QA.find(identifier) + len(identifier)
                    Q_end_index = QA[Q_begin_index:].find('\n')+Q_begin_index
                    break
        
            for ans_identifier in ans_identifiers:
                if ans_identifier in QA[Q_end_index:]:
                    A_begin_index = QA[Q_end_index:].find(identifier)+len(identifier)+Q_end_index
                    A_end_index = len(QA)
                    break

            Question = QA[Q_begin_index:Q_end_index].split('.', 1)[-1].split(':', 1)[-1].replace('**', '').strip()
            Answer = QA[A_begin_index:A_end_index].split(':', 1)[-1].replace('</s>','').replace('<|endoftext|>','').replace('<|eot_id|>', '').replace('<|im_end|>', '').replace('**', '').replace('\n-------------------------------------------', '').replace('-------', '').replace('----','').replace('**', '').strip()
            
            for ans_end_identifier in ans_end_identifiers:
                if len(Question) > 2 and len(Answer)>0:
                    if Answer[-1] == ans_end_identifier:
                        One_QA_dict={
                            "instruction" : Question,
                            "input": "",
                            "output": Answer,
                        }
                        
                        if Question in json_dataset_dict:
                            repeat_num += 1
                        else:
                            json_dataset_list.append(One_QA_dict)
                            json_dataset_dict[Question] = Answer
                            break
                else:
                    break
        
        return repeat_num, json_dataset_list

    except Exception as e:
            print(f"Error: Can't get the QA from response (An unexpected error occurred: {e})")


if __name__ == '__main__':
    FileFolder = "~/LLaMA-Factory/data"
    UploadFile = "~/LLaMA-Factory/data/Files/美利堅合眾國憲法.json"
    Name = "美利堅合眾國憲法"
    Language = "English"
    num_QandA = 9
    NoLimit_QandA = False
    
    producing = ProducingProcess(FileFolder = FileFolder,
                                 UploadFile = UploadFile,
                                 Name = Name,
                                 Language = Language,
                                 num_QandA = num_QandA,
                                 NoLimit_QandA = NoLimit_QandA)
    
    dataset_data = producing.start()
    print('dataset_data=', dataset_data)
    pass
