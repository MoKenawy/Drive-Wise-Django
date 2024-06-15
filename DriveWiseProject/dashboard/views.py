from django.shortcuts import render ,redirect
from django.template import loader
from django.shortcuts import render
from .utils.firebase_utils import FirebaseHelper
from DrivewiseApp.decorators import firebase_auth_required
from .forms import AddDriverForm
from django.core.files.storage import FileSystemStorage
from django.views import View

firebase_helper = FirebaseHelper()

@firebase_auth_required
def dashboard(request):
    drivers = firebase_helper.get_all_drivers_data()
    # test_driver = {'driver_id': "test_driver",
    #                'rating': 2.3}
    # drivers.append(test_driver)

    average_rate = calculate_average_ratings(drivers)
    leaderboard ,best_driver, worst_driver = get_driver_ranks(drivers)
    context = {'drivers': drivers,
                'average_rate':average_rate,
                'best_driver': best_driver,
                'worst_driver': worst_driver,
                'leaderboard': leaderboard}
    return render(request, 'dashboard.html', context)


def calculate_average_ratings(drivers_info):
    sum = 0
    for driver in drivers_info:
        if driver['rating'] != None:
            sum += driver['rating']
    avg = sum/(len(drivers_info))
    avg = round(avg, 3)
    return avg

def get_driver_ranks(drivers_info):
    # Sort drivers based on rating (descending order)
    sorted_drivers = sorted(drivers_info, key=lambda x: x['rating'], reverse=True)
    return sorted_drivers[:10] , sorted_drivers[0] , sorted_drivers[-1]

@firebase_auth_required
def driver_detail(request, driver_id):
    drivers = firebase_helper.get_all_drivers_data()  # Retrieve all drivers
    driver_data = firebase_helper.get_driver_data(driver_id)
    violations_stats = firebase_helper.get_violations_stats(driver_id)

    context = {
        'drivers': drivers,  # Pass all drivers to the template
        'driver_id': driver_id,
        'driver_data': driver_data,
        'violations_stats': violations_stats
    }
    print(violations_stats.get('drowsiness_violation_count'))
    return render(request, 'driver_detail.html', context)


class AddDriverView(View):
    def get(self, request):
        form = AddDriverForm()
        return render(request, 'add_driver.html', {'form': form})

    def post(self, request):
        form = AddDriverForm(request.POST, request.FILES)
        if form.is_valid():
            driver_data = form.cleaned_data
            # if 'photo' in request.FILES:
            #     photo = request.FILES['photo']
            #     fs = FileSystemStorage()
            #     filename = fs.save(photo.name, photo)
            #     driver_data['photo'] = fs.url(filename)
            # else:
            #     driver_data['photo'] = None
            firebase_helper.add_driver(request,driver_data)
            return redirect('dashboard')
        return render(request, 'add_driver.html', {'form': form})
