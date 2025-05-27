from django.shortcuts import render
from .knowledge.rule_engine import get_recommendation
from .knowledge.semantic_network import find_related_careers
from .knowledge.ontology import load_career_ontology, query_career_requirements
from .knowledge.nlp_module import extract_keywords
from .knowledge.ai_analysis import analyze_career_fit
# from .knowledge.frames import career_frames # Ensure this is present
from .data_loader import load_careers_from_csv # New import for CSV data
from .knowledge.online_search import fetch_career_info, get_search_urls # New imports

def career_recommendation(request):
    context = {} # Initialize context earlier

    # Load career data from CSV and prepare for lookup
    all_careers_data_list = load_careers_from_csv()
    careers_by_title = {career['title']: career for career in all_careers_data_list}

    if request.method == 'POST':
        # Retrieve form data
        current_skills = request.POST.get('current_skills', '')
        current_courses = request.POST.get('current_courses', '')
        learning_aspirations = request.POST.get('learning_aspirations', '')
        description = request.POST.get('description', '')  # free-text description

        # Use NLP to extract additional keywords
        description_keywords = extract_keywords(description)
        courses_keywords = extract_keywords(current_courses)
        aspirations_keywords = extract_keywords(learning_aspirations)

        # Combine all keywords for profile_data
        all_skills_keywords = [skill.strip() for skill in current_skills.split(',') if skill.strip()] + \
                              description_keywords + \
                              courses_keywords + \
                              aspirations_keywords
        
        profile_data = {
            'skills': all_skills_keywords,
            # 'education': education.strip(), # Removed
            # 'interests': [interest.strip() for interest in interests.split(',') if interest.strip()] # Removed
        }

        # Rule-based recommendation (can be kept for secondary purposes or removed)
        # recommendation_old = get_recommendation(profile_data)

        # AI Analysis (Primary)
        ai_labels, ai_scores = analyze_career_fit(description) # Expects lists of labels and scores
        
        ai_recommendations = []
        N = 3 # Top 3 recommendations

        if ai_labels: # Check if there are any AI recommendations
            for i in range(min(N, len(ai_labels))):
                career_title = ai_labels[i]
                score = ai_scores[i]
                
                # Fetch details from CSV data
                career_detail = careers_by_title.get(career_title) # This will now be a dictionary or None
                # Fetch info from web
                online_info = fetch_career_info(career_title)   
                # Get search URLs
                search_urls = get_search_urls(career_title)     

                ai_recommendations.append({
                    'title': career_title,
                    'score': score,
                    'details': career_detail, # This will now be a dictionary or None
                    'online_info': online_info,
                    'search_urls': search_urls,
                })
            context['best_match'] = ai_recommendations[0] if ai_recommendations else None
        
        context['ai_recommendations'] = ai_recommendations
        
        # Consolidate all extracted keywords for the context
        all_extracted_keywords_for_context = description_keywords + courses_keywords + aspirations_keywords
        context['nlp_keywords'] = all_extracted_keywords_for_context

        # --- Deprioritize or comment out old context variables ---
        # context['recommendation'] = recommendation_old # Old rule-based
        # context['ai_analysis'] = {"label": ai_labels[0] if ai_labels else None, "score": ai_scores[0] if ai_scores else None} # Old single AI result

        # Related careers using semantic network (can be kept or removed)
        # related = []
        # if profile_data['skills']:
        #     for skill_item in profile_data['skills']:
        #         if isinstance(skill_item, str) and skill_item.strip():
        #             related.extend(find_related_careers(skill_item))
        # context['related_careers'] = list(set(related))

        # Ontology query (can be kept or removed)
        # ontology_results = []
        # if recommendation_old: 
        #     g = load_career_ontology()
        #     if isinstance(recommendation_old, str) and recommendation_old.strip():
        #          ontology_results = query_career_requirements(g, recommendation_old.replace(" ", ""))
        #     elif isinstance(recommendation_old, list) and recommendation_old:
        #          ontology_results = query_career_requirements(g, recommendation_old[0].replace(" ", ""))
        # context['ontology_info'] = ontology_results
        
    return render(request, 'advisor/recommendations.html', context)
