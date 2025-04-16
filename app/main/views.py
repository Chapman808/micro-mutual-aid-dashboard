from . import main
from .forms import ProfileForm
from flask import make_response, render_template
import dao

@main.route('/', methods=['GET', 'POST'])
def index(requireActions : bool = None):
  cards = dao.get_profiles()
  return render_template('index.html', cards = cards)

@main.route('/form', methods=['GET', 'POST'])
def index(requireActions : bool = None):
  form = ProfileForm()
  if form.validate_on_submit():
    profile_data = form.expansions.data #add to form later
    print(profile_data)
  return render_template('edit_profile.html', form=form)

