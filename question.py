import os


current_directory = os.path.dirname(os.path.realpath(__file__))

intents_and_question = {

        "greet":  [

            "hey",
            "hello",
            "Hello?",
            "hello?",
            "hi",
            "hello there",
            "good morning",
            "good evening",
            "moin",
            "hey there",
            "let's go",
            "hey dude",
            "goodmorning",
            "goodevening",
            "good afternoon"
        ],
    

    
        "appointment_booking": [

            "How can I schedule an appointment",
            "I need to book an appointment with a doctor",
            "what's the procedure for booking an appointment",
            "hello, I'd like to schedule an appointment.",
            "book an appointment",
            "appointment",
            "need an appointment"
        ],


        "doctor_information": [

            "tell me more about dr. abc",
            "what's the specialty of dr. abc",
            "give me the contact details for dr. abc"
            "doctor",
            "contact doctor",
            "doctor contact",
            "doctor detail",
            "detail doctor"

        ],


        "department_information": [

            "which departments are available in the hospital",
            "can you provide details about the cardiology department",
            "tell me more about the pediatric department",
            "department",
            "which department",
            "department info"

        ],


        "visiting_hours":[

            "what are the visiting hours for patients",
            "when can I visit a patient in the hospital",
            "is there a specific time for visiting hours",
            "visiting time",
            "visit",
            "time",
            "time to visit",
            "visit time",
            "hospital visit",
            "visit hospital"
        ],


        "location_and_directions":[

            "how do I get to the hospital",
            "can you provide me with directions to your location",
            "where is the hospital situated",
            "direction",
            "direction hospital",
            "hospital direction",
            "location",
            "hospital location"
        ],


        "billing_and_insurance": [

            "how do I pay my medical bills",
            "do you accept my insurance",
            "what's the billing process for a hospital stay",
            "bills",
            "insurance",
            "pay bill",
        ],


        "medical_records": [
            "how can I access my medical records",
            "request my medical history",
            "I need a copy of my lab results",
            "medical records",
            "medical record",
            "record",
            "records",
            "record medical",
            "results",
            "lab results",
            "result copy",
            "copy result"
        ],


        "emergency_services": [
            "what should I do in case of a medical emergency",
            "how do I contact the hospital in an emergency",
            "tell me about your emergency services",
            "emergency",
            "emergency service"
        ],


        "covid19_information": [
            "what safety measures are in place due to COVID-19",
            "is it safe to visit the hospital during the pandemic",
            "do you offer COVID-19 testing or vaccinations",
            "covid19"

        ],


        "feedback_and_complaints": [
            "I want to provide feedback about my experience",
            "how can I file a complaint about a staff member",
            "share my thoughts on my recent visit",
            "feedback",
            "complaints",
            "complain",
            "share thoughts",
            "experiance"
        ],


        "general_information": [
            "tell me more about the hospital",
            "what services do you offer",
            "is there a cafeteria in the hospital",
            "information",
            "cafeteria",
            "services",
            "services offered",
            "offered services"
        ]

}


'''video_urls = {

            "greet": "/home/knight/ChatBot_UI/video/greet.mp4",
            "appointment_booking": "/home/knight/ChatBot_UI/video/appointment_booking.mp4",
            "doctor_information": "/home/knight/ChatBot_UI/video/doctor_information.mp4",
            "department_information": "/home/knight/ChatBot_UI/video/department_information.mp4",
            "visiting_hours": "/home/knight/ChatBot_UI/video/visiting_hours.mp4",
            "location_and_directions": "/home/knight/ChatBot_UI/video/location_and_directions.mp4",
            "billing_and_insurance": "/home/knight/ChatBot_UI/video/billing_and_insurance.mp4",
            "medical_records": "/home/knight/ChatBot_UI/video/medical_records.mp4",
            "emergency_assistance": "/home/knight/ChatBot_UI/video/emergency_services.mp4",
            "covid19_information": "/home/knight/ChatBot_UI/video/covid19_information.mp4",
            "feedback_and_complaints": "/home/knight/ChatBot_UI/video/feedback_and_complaints.mp4",
            "thank_you": "/home/knight/ChatBot_UI/video/thank_you.mp4",
            "general_information": "/home/knight/ChatBot_UI/video/general_information.mp4"
        
        
        }'''



video_urls = {

            "greet": os.path.join(current_directory, 'video', 'greet.mp4'),
            "appointment_booking": os.path.join(current_directory, 'video', 'appointment_booking.mp4'),
            "doctor_information": os.path.join(current_directory, 'video', 'doctor_information.mp4'),
            "department_information": os.path.join(current_directory, 'video' ,'department_information.mp4'),
            "visiting_hours": os.path.join(current_directory, 'video', 'visiting_hours.mp4'),
            "location_and_directions": os.path.join(current_directory, 'video','location_and_directions.mp4'),
            "billing_and_insurance": os.path.join(current_directory, 'video', 'billing_and_insurance.mp4'),
            "medical_records": os.path.join(current_directory, 'video', 'medical_records.mp4'),
            "emergency_assistance": os.path.join(current_directory, 'video','emergency_services.mp4'),
            "covid19_information": os.path.join(current_directory, 'video','covid19_information.mp4'),
            "feedback_and_complaints": os.path.join(current_directory, 'video','feedback_and_complaints.mp4'),
            "thank_you": os.path.join(current_directory, 'video','video/thank_you.mp4'),
            "general_information": os.path.join(current_directory, 'video','general_information.mp4')
        
        
        }


def get_video_response(intent):

    return video_urls.get(intent)



#print(get_video_response('greet'))




