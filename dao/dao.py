import pickle

def get_profiles():
  try:
    with open ('data/profiles.pkl', 'rb') as profiles:
      profiles = pickle.load(profiles)
      profiles = dict(profiles)
  except Exception as e:
    print("ERROR: Could not load profiles.pkl file from data")
    raise e
  return profiles


def set_profile(name : str, needs : str, provides : str) -> None:
  try:
    profiles = get_profiles()
  except Exception as e:
    print(e)
    print('could not load profiles. Initializing new profile file')
    profiles = {}
  profiles[name] = {'needs' : needs, 'provides' : provides}
  with open ('data/profiles.pkl', 'wb') as profiles_file:
      pickle.dump(profiles, profiles_file)

