
def automation_1(data):
    injection_data_title=data['title']
    injection_data_auth=data['auth']
    injection_data_dis=data['dis']
    #need to add the discription
    #for that i need to find the correct node element
    injection_code=f"document.getElementById('data-title').value={injection_data_title} \n document.getElementById('data-primary-author-first-name').value={injection_data_auth}"
    