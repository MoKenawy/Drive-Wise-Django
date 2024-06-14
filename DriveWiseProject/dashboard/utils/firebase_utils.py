from firebase_admin import db
from firebase_admin import storage

class FirebaseHelper:
    def __init__(self):
        self.ref = db.reference()
        self.bucket = storage.bucket()

    def get_all_drivers_data(self):
        drivers = self.ref.child('drivers').get()
        drivers_data = []
        for driver_id, data in drivers.items():
            driver_info = {
                'driver_id': driver_id,
                'rating': data.get('rating')
            }
            drivers_data.append(driver_info)
        return drivers_data

    def get_driver_data(self, driver_id):
        self.ref.child('drivers').child(driver_id)
        return self.ref.child('drivers').child(driver_id).get()

    def get_driver_data(self, driver_id):
        return self.ref.child('drivers').child(driver_id).get()

    def get_violations_stats(self, driver_id):
        driver_data = self.get_driver_data(driver_id)
        violations_count = 0
        speed_violation_count = 0
        distance_violation_count = 0
        drowsiness_violation_count = 0
        violations_history = None
        try:
            if 'violations' in driver_data:
                violations_count = len(driver_data['violations'])
                violation_ref = self.ref.child('drivers').child(driver_id).child('violations')
                violations_history = violation_ref.get().items()

                for violation_id, violation_data in violation_ref.get().items():
                    violation_type = violation_data.get('type')
                    if violation_type == 'speed_violation':
                        speed_violation_count += 1
                    elif violation_type == 'distance_violation':
                        distance_violation_count += 1
                    elif violation_type == 'drowsiness_violation':
                        drowsiness_violation_count += 1
        except Exception as e:
            print(e)

        violations_stats = {
            'violations_count': violations_count,
            'speed_violation_count': speed_violation_count,
            'distance_violation_count': distance_violation_count,
            'drowsiness_violation_count': drowsiness_violation_count,
            'violations_history':violations_history
        }

        return violations_stats
    


    def get_top_records(self, ref):
        
        try:
            ref.get
            snapshot = ref.order_by_child(ref.child('time')).limit_to_last(5).get()
            records = []
            for key, val in snapshot.items():
                records.append({'key': key, **val})

            # Sorting the records in descending order (because limit_to_last sorts in ascending order)
            records.sort(key=lambda x: x['value'], reverse=True)
            
            for record in records:
                print(record)
            return records
        except Exception as error:
            print('Error fetching records:', error)
            raise error

    def add_driver(self, request,driver_data):
        driver_id = driver_data['driver_id']
        driver_info = {
            'email': driver_data['email'],
            'first_name': driver_data['first_name'],
            'last_name': driver_data['last_name'],
            'phone_number': driver_data['phone_number'],
            'address': driver_data['address'],
            'birth_date': str(driver_data['birth_date']),
            'rating': 5,
        }
        if driver_data.get('photo'):
            image_file = request.FILES.get('photo')
            print(image_file)
            image_url = self.upload_driver_image(driver_id,image_file)
            driver_info['photo'] = image_url
            # Get a reference to the storage service, which is used to create references in your storage bucket

        self.ref.child('drivers').child(driver_id).set(driver_info)


    def upload_driver_image(self, driver_id,  image_file):
        image_name = f"{driver_id}_{image_file.name}"
        blob = self.bucket.blob(f"images/{image_name}")
        blob.upload_from_file(image_file)

        # Get public URL of the uploaded image
        image_url = blob.public_url
        return image_url