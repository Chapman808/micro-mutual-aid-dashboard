from . import main
from .forms import ProfileForm
from flask import make_response, render_template
import dao.dao as dao

@main.route('/', methods=['GET', 'POST'])
def index(requireActions : bool = None):
  cards = dao.get_profiles()
  return render_template('index.html', cards = cards)

@main.route('/form', methods=['GET', 'POST'])
def form(requireActions : bool = None):
  form = ProfileForm()
  if form.validate_on_submit():
    profile_data = form.data #add to form later
    print(profile_data)
    name = profile_data['name']
    needs = profile_data['needs']
    provides = profile_data['provides']
    dao.set_profile(name, needs, provides)
  return render_template('edit_profile.html', form=form)

