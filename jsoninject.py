import json

def find_emails_and_passwords(obj):
    result_list = []

    if isinstance(obj, dict):
        email = obj.get('email', '')
        password = obj.get('password', '')
        id_value = obj.get('id', '')
        username = obj.get('username', '')
        name = obj.get('name', '')
        dob = obj.get('dob', '')
        phone = obj.get('phone', '')
        address = obj.get('address', '')
        source = obj.get('source', '')
        breach_date = obj.get('breach_date', '')
        domain_name = obj.get('domainName', '')
        others = obj.get('others', '')

        if '@' in email:
            result_list.append({
                "id": id_value,
                "username": username,
                "email": email,
                "password": password,
                "password_hash": password,
                "name": name,
                "dob": dob,
                "phone": phone,
                "address": address,
                "source": source,
                "breach_date": breach_date,
                "domainName": domain_name,
                "others": others
            })

        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                sub_results = find_emails_and_passwords(value)
                result_list.extend(sub_results)

    elif isinstance(obj, list):
        for item in obj:
            sub_results = find_emails_and_passwords(item)
            result_list.extend(sub_results)

    return result_list

def read_and_find_emails_and_passwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    result_list = find_emails_and_passwords(json_data)
    return result_list

def save_to_json(output_file_path, data):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(data, output_file, indent=2)
        print(f'Found Email Addresses and Passwords saved to {output_file_path}')
    except Exception as e:
        print(f'Error saving to JSON file: {e}')

def main():
    input_file_path = 'C:\\Users\\Gaurav Kumar\\Desktop\\testing\\test.json'
    result_list = read_and_find_emails_and_passwords(input_file_path)

    output_file_path = 'C:\\Users\\Gaurav Kumar\\Desktop\\testing\\emails_and_passwords.json'
    save_to_json(output_file_path, result_list)

if __name__ == "__main__":
    main()
