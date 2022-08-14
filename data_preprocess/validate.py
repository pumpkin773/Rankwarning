import os
import csv

if __name__ == '__main__':
    # path = 'D:\\data\\FixedViolations\\Types\\'
    # type_list = os.listdir(path)
    # count = 0
    # for i in type_list:
    #     with open(path + i + '\\Tokens.list', 'r') as f:
    #         count = count + len(f.readlines())
    #     f.close()
    # print(count)
    # str = 'SwitchStatement switch VariableName statusCode SwitchCase case NumberLiteral numberLiteral VariableName message Operator = StringLiteral stringLiteral VariableName httpsessionVar MethodName setAttribute StringLiteral stringLiteral VariableName message BreakStatement break SwitchCase case NumberLiteral numberLiteral VariableName error Operator = StringLiteral stringLiteral VariableName httpsessionVar MethodName setAttribute StringLiteral stringLiteral VariableName error VariableName httpservletresponseVar MethodName sendRedirect StringLiteral stringLiteral ReturnStatement return SwitchCase case NumberLiteral numberLiteral VariableName error Operator = StringLiteral stringLiteral VariableName httpsessionVar MethodName setAttribute StringLiteral stringLiteral VariableName error BreakStatement break SwitchCase case NumberLiteral numberLiteral SimpleType StringWriter VariableName stringwriterVar New new SimpleType StringWriter SimpleType InputStream VariableName inputstreamVar VariableName httpentityVar MethodName getContent Name IOUtils MethodName copy VariableName readingStream VariableName writer StringLiteral stringLiteral SimpleType String VariableName stringVar VariableName writer MethodName toString SimpleType Gson VariableName gsonVar New new SimpleType Gson SimpleType Type VariableName typeVar New new ParameterizedType TypeToken AnonymousClassDeclaration AnonymousClass MethodName getType ParameterizedType ArrayList VariableName arraylistVar VariableName gson MethodName fromJson VariableName responseString VariableName listType VariableName message Operator = StringLiteral stringLiteral EnhancedForStatement for SimpleType String VariableName stringVar VariableName postList ArrayType String[] VariableName string[]Var VariableName postDropped MethodName split StringLiteral stringLiteral VariableName message Operator += StringLiteral stringLiteral Operator + VariableName valuesSplit NumberLiteral numberLiteral StringLiteral stringLiteral VariableName postcontrollerVar MethodName removeAppliedPost Name Integer MethodName parseInt VariableName valuesSplit NumberLiteral numberLiteral VariableName message Operator = VariableName message MethodName substring NumberLiteral numberLiteral VariableName message MethodName lastIndexOf StringLiteral stringLiteral VariableName httpsessionVar MethodName setAttribute StringLiteral stringLiteral VariableName message'
    # print(len(str.split(' ')))
    report_dir = 'D:\\graduated_design\\data_preprocess\\Exp\\maven-dependency-plugin\\result\\positive_reports\\'
    file_list = os.listdir(report_dir)
    print('All positive_reports: ' + str(len(file_list)))
    all_counter = 0
    for file in file_list:
        file_path = report_dir + file
        counter = 0
        flag = False
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[8] == '1':
                    flag = True
                    counter += 1
        f.close()
        if not flag:
            print(file + ': has no positive warning!')
        else:
            print(file + ': ' + str(counter))
        all_counter += counter
    print('-------------------------------------')
    print('All positive warning: ' + str(all_counter))

