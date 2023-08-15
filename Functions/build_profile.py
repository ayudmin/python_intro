def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile('ayume', 'francis', location='juba', profession='wed developer/forex trader')
print(user_profile)

ayudmin = build_profile(first_name='Ayudmin', last_name='Ayudmin', profession='System Administrator', Account_balance='$0.0')
print(ayudmin)