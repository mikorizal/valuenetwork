from django.conf.urls import patterns, url


urlpatterns = patterns("",
    url(r"^start/$", 'valuenetwork.valueaccounting.views.start', name="start"),
    url(r"^projects/$", 'valuenetwork.valueaccounting.views.projects', name="projects"),
    url(r"^agents/$", 'valuenetwork.valueaccounting.views.agents', name="agents"),
    #url(r"^create-project/$", 'valuenetwork.valueaccounting.views.create_project', name="create_project"),
    url(r"^resources/$", 'valuenetwork.valueaccounting.views.resource_types', name="resource_types"),
    url(r"^resource-type/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.resource_type', name="resource_type"),
    url(r"^inventory/$", 'valuenetwork.valueaccounting.views.inventory', name="inventory"),
    url(r"^all-contributions/$", 'valuenetwork.valueaccounting.views.all_contributions', name="all_contributions"),
    url(r"^contributions/(?P<project_id>\d+)/$", 'valuenetwork.valueaccounting.views.contributions', name="contributions"),
    url(r"^contributionhistory/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.contribution_history', name="contribution_history"),
    url(r"^agent-stats/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.agent_stats', name="agent_stats"),
    url(r"^project-wip/(?P<project_id>\d+)/$", 'valuenetwork.valueaccounting.views.project_wip', name="project_wip"),
    url(r"^finished-processes/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.finished_processes', name="finished_processes"),
    url(r"^value/(?P<project_id>\d+)/$", 'valuenetwork.valueaccounting.views.value_equation', name="value_equation"),
    url(r"^xbomfg/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.extended_bill', name="extended_bill"),
    url(r"^edit-xbomfg/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.edit_extended_bill', name="edit_extended_bill"),
    url(r"^edit-stream-recipe/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.edit_stream_recipe', name="edit_stream_recipe"),
    url(r"^view-stream-recipe/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.view_stream_recipe', name="view_stream_recipe"),
    url(r"^network/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.network', name="network"),
    url(r"^project-network/$", 'valuenetwork.valueaccounting.views.project_network', name="project_network"),
    url(r"^timeline/$", 'valuenetwork.valueaccounting.views.timeline', name="timeline"),
    url(r"^jsontimeline/$", 'valuenetwork.valueaccounting.views.json_timeline', name="json_timeline"),
    url(r"^json-processes/$", 'valuenetwork.valueaccounting.views.json_processes', name="json_processes"),
    url(r"^json-processes/(?P<order_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_processes', name="json_processes"),   
    url(r"^json-project-processes/$", 'valuenetwork.valueaccounting.views.json_project_processes', name="json_project_processes"),
    url(r"^json-project-processes/(?P<object_type>\w{1})/(?P<object_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_project_processes', name="json_project_processes"),
    url(r"^order-graph/(?P<order_id>\d+)/$", 'valuenetwork.valueaccounting.views.order_graph', name="order_graph"),
    url(r"^processes-graph/$", 'valuenetwork.valueaccounting.views.processes_graph', name="processes_graph"),
    url(r"^processes-graph/(?P<object_type>\w{1})/(?P<object_id>\d+)/$", 'valuenetwork.valueaccounting.views.processes_graph', name="processes_graph"),
    url(r"^radial-graph/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.radial_graph', name="radial_graph"),
    url(r"^create-processtype-input/(?P<process_type_id>\d+)/(?P<slot>\w{1})/$", 'valuenetwork.valueaccounting.views.create_process_type_input', 
        name="create_process_type_input"),
    url(r"^create-processtype-citable/(?P<process_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_process_type_citable', 
        name="create_process_type_citable"),
    url(r"^create-processtype-work/(?P<process_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_process_type_work', 
        name="create_process_type_work"),
    url(r"^create-processtype-feature/(?P<process_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_process_type_feature', 
        name="create_process_type_feature"),
    url(r"^change-feature/(?P<feature_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_feature', 
        name="change_feature"),
    url(r"^delete-feature-confirmation/(?P<feature_id>\d+)/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_feature_confirmation', 
        name="delete_feature_confirmation"),
    url(r"^delete-feature/(?P<feature_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_feature', 
        name="delete_feature"),
    url(r"^create-options-for-feature/(?P<feature_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_options_for_feature', 
        name="create_options_for_feature"),
    url(r"^change-options-for-feature/(?P<feature_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_options_for_feature', 
        name="change_options_for_feature"),
    url(r"^change-processtype-input/(?P<input_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_process_type_input', 
        name="change_process_type_input"),
    url(r"^create-agent/$", 'valuenetwork.valueaccounting.views.create_agent', 
        name="create_agent"),
    url(r"^create-agent-resource-type/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_agent_resource_type', 
        name="create_agent_resource_type"),
    url(r"^change-agent-resource-type/(?P<agent_resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_agent_resource_type', 
        name="change_agent_resource_type"),
    url(r"^create-process-type-for-resource-type/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_process_type_for_resource_type', 
        name="create_process_type_for_resource_type"),
    url(r"^create-process-type-for-streaming/(?P<resource_type_id>\d+)/(?P<process_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_process_type_for_streaming', 
        name="create_process_type_for_streaming"),
    url(r"^create-process-type-for-streaming/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_process_type_for_streaming', 
        name="create_process_type_for_streaming"),
    url(r"^change-process-type/(?P<process_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_process_type', 
        name="change_process_type"),
    url(r"^change-resource-type/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_resource_type', 
        name="change_resource_type"),
    url(r"^create-resource-type/$", 'valuenetwork.valueaccounting.views.create_resource_type', 
        name="create_resource_type"),
    url(r"^create-rt-ajax/$", 'valuenetwork.valueaccounting.views.create_resource_type_ajax', 
        name="create_resource_type_ajax"),
    url(r"^create-rt-sp-ajax/$", 'valuenetwork.valueaccounting.views.create_resource_type_simple_patterned_ajax', 
        name="create_resource_type_simple_patterned_ajax"),
    url(r"^delete-resource-type/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_resource_type', 
        name="delete_resource_type"),
    url(r"^delete-resource-type-confirmation/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_resource_type_confirmation', 
        name="delete_resource_type_confirmation"),
    url(r"^delete-resource/(?P<resource_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_resource', 
        name="delete_resource"),
    url(r"^delete-process-type/(?P<process_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_process_type', 
        name="delete_process_type"),
    url(r"^delete-process-type-confirmation/(?P<process_type_id>\d+)/(?P<resource_type_id>\d+)/$", 
        'valuenetwork.valueaccounting.views.delete_process_type_confirmation', 
        name="delete_process_type_confirmation"),
    url(r"^delete-process-input/(?P<process_input_id>\d+)/(?P<resource_type_id>\d+)/$", 
        'valuenetwork.valueaccounting.views.delete_process_input', 
        name="delete_process_input"),
    url(r"^delete-process-type-input/(?P<process_input_id>\d+)/(?P<resource_type_id>\d+)/$", 
        'valuenetwork.valueaccounting.views.delete_process_type_input', 
        name="delete_process_type_input"),
    url(r"^delete-source/(?P<source_id>\d+)/(?P<resource_type_id>\d+)/$", 
        'valuenetwork.valueaccounting.views.delete_source', 
        name="delete_source"),
    url(r"^json-resourcetype-unit/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_resource_type_unit', 
        name="json_resource_type_unit"),
    url(r"^json-directional-unit/(?P<resource_type_id>\d+)/(?P<direction>\w+)/$", 'valuenetwork.valueaccounting.views.json_directional_unit', 
        name="json_directional_unit"),
    url(r"^json-directional-unit-and-rule/(?P<resource_type_id>\d+)/(?P<direction>\w+)/$", 'valuenetwork.valueaccounting.views.json_directional_unit_and_rule', 
        name="json_directional_unit_and_rule"),
    url(r"^json-resourcetype-defaults/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_resource_type_defaults', 
        name="json_resource_type_defaults"),
     url(r"^json-agent/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_agent', 
        name="json_agent"),
    url(r"^create-order/$", 'valuenetwork.valueaccounting.views.create_order', name="create_order"),
    url(r"^change-order/(?P<order_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_order', name="change_order"),
    url(r"^order-schedule/(?P<order_id>\d+)/$", 'valuenetwork.valueaccounting.views.order_schedule', name="order_schedule"),
    url(r"^delete-order/(?P<order_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_order', name="delete_order"),
    url(r"^delete-order-confirmation/(?P<order_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_order_confirmation', name="delete_order_confirmation"),
    url(r"^demand/$", 'valuenetwork.valueaccounting.views.demand', name="demand"),
    url(r"^supply/$", 'valuenetwork.valueaccounting.views.supply', name="supply"),
    url(r"^work/$", 'valuenetwork.valueaccounting.views.work', name="work"),
    url(r"^schedule/$", 'valuenetwork.valueaccounting.views.schedule', name="schedule"),
    url(r"^schedule/(?P<context_agent_slug>[-\w]+)/$", 'valuenetwork.valueaccounting.views.schedule', name="schedule"),
    url(r"^project-stats/(?P<context_agent_slug>[-\w]+)/$", 'valuenetwork.valueaccounting.views.project_stats', name="project_stats"),
    url(r"^project-roles/(?P<context_agent_slug>[-\w]+)/$", 'valuenetwork.valueaccounting.views.project_roles', name="project_roles"),
    url(r"^commit-to-task/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.commit_to_task', 
        name="commit_to_task"),
    url(r"^uncommit/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.uncommit', 
        name="uncommit"),
    url(r"^change-process-sked-ajax/$", 'valuenetwork.valueaccounting.views.change_process_sked_ajax', 
        name="change_process_sked_ajax"),
    url(r"^past-work/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.log_past_work', 
        name="log_past_work"),
    url(r"^pastwork-reload/(?P<commitment_id>\d+)/(?P<event_id>\d+)/(?P<was_running>\d+)/(?P<was_retrying>\d+)/$", 'valuenetwork.valueaccounting.views.pastwork_reload', 
        name="pastwork_reload"),
    url(r"^labnotes-reload/(?P<commitment_id>\d+)/(?P<was_running>\d+)/(?P<was_retrying>\d+)/$", 'valuenetwork.valueaccounting.views.labnotes_reload', 
        name="labnotes_reload"),
    url(r"^work-commitment/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.work_commitment', 
        name="work_commitment"),
    url(r"^work-now/(?P<process_id>\d+)/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.work_now', 
        name="work_now"),
    url(r"^change-commitment/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_commitment', 
        name="change_commitment"),
    url(r"^forward-schedule-source/(?P<commitment_id>\d+)/(?P<source_id>\d+)/$", 'valuenetwork.valueaccounting.views.forward_schedule_source', 
        name="forward_schedule_source"),
    url(r"^forward-schedule-process/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.forward_schedule_process', 
        name="forward_schedule_process"),
    url(r"^save-labnotes/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.save_labnotes', 
        name="save_labnotes"),
    url(r"^save-work-now/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.save_work_now', 
        name="save_work_now"),
    url(r"^save-past-work/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.save_past_work', 
        name="save_past_work"),
    #url(r"^process/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.process_details', name="process_details"),
    #url(r"^process-logging/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.process_oriented_logging', name="process_oriented_logging"),
    url(r"^process/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.process_oriented_logging', name="process_details"),
    url(r"^process-finished/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.process_finished', name="process_finished"),
    url(r"^process-done/$", 'valuenetwork.valueaccounting.views.process_done', name="process_done"),
    url(r"^work-done/$", 'valuenetwork.valueaccounting.views.work_done', 
        name="work_done"),
    url(r'^log-resource/(?P<commitment_id>\d+)/$', 'valuenetwork.valueaccounting.views.log_resource_for_commitment', 
        name="log_resource_for_commitment"),
    url(r'^add-to-resource/(?P<commitment_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_to_resource_for_commitment', 
        name="add_to_resource_for_commitment"),
    url(r'^production-event/$', 'valuenetwork.valueaccounting.views.production_event_for_commitment', 
        name="production_event_for_commitment"),
    url(r'^resource-event/(?P<commitment_id>\d+)/$', 'valuenetwork.valueaccounting.views.resource_event_for_commitment', 
        name="resource_event_for_commitment"),
    url(r'^work-event/(?P<commitment_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_work_event', 
        name="add_work_event"),
    url(r'^unplanned-work-event/(?P<process_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_unplanned_work_event', 
        name="add_unplanned_work_event"),
    url(r'^unplanned-output-event/(?P<process_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_unplanned_output', 
        name="add_unplanned_output"),
    url(r'^consumption-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_consumption_event', 
        name="add_consumption_event"),
    url(r'^use-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_use_event', 
        name="add_use_event"),
    url(r'^citation-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$', 'valuenetwork.valueaccounting.views.log_citation', 
        name="log_citation"),
    url(r'^unplanned-cite-event/(?P<process_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_unplanned_cite_event', 
        name="add_unplanned_cite_event"),
    url(r'^consumption-event/$', 'valuenetwork.valueaccounting.views.consumption_event_for_commitment', 
        name="consumption_event_for_commitment"),
    url(r'^unplanned-input-event/(?P<process_id>\d+)/(?P<slot>\w{1})/$', 'valuenetwork.valueaccounting.views.add_unplanned_input_event', 
        name="add_unplanned_input_event"),
    url(r'^time-use-event/$', 'valuenetwork.valueaccounting.views.time_use_event_for_commitment', 
        name="time_use_event_for_commitment"),
    url(r"^failed-outputs/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.failed_outputs', 
        name="failed_outputs"),
    url(r"^new-process-output/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.new_process_output', 
        name="new_process_output"),
    url(r"^new-process-input/(?P<commitment_id>\d+)/(?P<slot>\w{1})/$", 'valuenetwork.valueaccounting.views.new_process_input', 
        name="new_process_input"),
    url(r"^new-process-citation/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.new_process_citation', 
        name="new_process_citation"),
    url(r"^new-process-worker/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.new_process_worker', 
        name="new_process_worker"),
    url(r"^log-stage-change-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$", 'valuenetwork.valueaccounting.views.log_stage_change_event', 
        name="log_stage_change_event"),
    url(r"^add-process-output/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.add_process_output', 
        name="add_process_output"),
    url(r"^add-process-input/(?P<process_id>\d+)/(?P<slot>\w{1})/$", 'valuenetwork.valueaccounting.views.add_process_input', 
        name="add_process_input"),
    url(r"^add-process-citation/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.add_process_citation', 
        name="add_process_citation"),
    url(r"^add-process-worker/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.add_process_worker', 
        name="add_process_worker"),        
    url(r"^delete-commitment/(?P<commitment_id>\d+)/(?P<labnotes_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_commitment', 
        name="delete_commitment"),
    url(r"^delete-process-commitment/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_process_commitment', 
        name="delete_process_commitment"),
    url(r"^citation-event-for-commitment/$", 'valuenetwork.valueaccounting.views.citation_event_for_commitment', 
        name="citation_event_for_commitment"),
    url(r"^create-process/$", 'valuenetwork.valueaccounting.views.create_process', 
        name="create_process"),
    url(r"^delete-process/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_process', 
        name="delete_process"),
    url(r"^process-selections/$", 'valuenetwork.valueaccounting.views.process_selections', 
        name="process_selections"),
    url(r"^process-selections/(?P<rand>\d+)/$", 'valuenetwork.valueaccounting.views.process_selections', 
        name="process_selections"),
    url(r"^plan-from-recipe/$", 'valuenetwork.valueaccounting.views.plan_from_recipe', 
        name="plan_from_recipe"),
    url(r"^plan-from-rt/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.plan_from_rt', 
        name="plan_from_rt"),
    url(r"^plan-from-rt-recipe/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.plan_from_rt_recipe', 
        name="plan_from_rt_recipe"),
    url(r"^change-process/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_process', 
        name="change_process"),
    url(r"^copy-process/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.copy_process', 
        name="copy_process"),
    url(r"^create-rand/$", 'valuenetwork.valueaccounting.views.create_rand', 
        name="create_rand"),
    url(r"^change-rand/(?P<rand_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_rand', 
        name="change_rand"),
    url(r"^copy-rand/(?P<rand_id>\d+)/$", 'valuenetwork.valueaccounting.views.copy_rand', 
        name="copy_rand"),
    url(r"^labnotes/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.labnotes', 
        name="labnotes"),
    url(r"^labnote/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.labnote', 
        name="labnote"),
    url(r"^resource/(?P<resource_id>\d+)/$", 'valuenetwork.valueaccounting.views.resource', 
        name="resource"),
    url(r"^incoming-value-flows/(?P<resource_id>\d+)/$", 'valuenetwork.valueaccounting.views.incoming_value_flows', 
        name="incoming_value_flows"),
    url(r"^unscheduled-time/$", 'valuenetwork.valueaccounting.views.unscheduled_time_contributions', 
        name="unscheduled_time"),
    url(r"^json-resourcetype-resources/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_resource_type_resources', 
        name="json_resource_type_resources"),
    url(r"^json-resourcetype-resources-locations/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_resource_type_resources_with_locations', 
        name="json_resource_type_resources_with_locations"),
    url(r"^json-resource/(?P<resource_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_resource', name="json_resource"),
    #url(r"^create-resource/(?P<resource_type_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_resource', 
    #    name="create_resource"),
    url(r"^change-resource/(?P<resource_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_resource', 
        name="change_resource"),
    url(r"^change-work-event/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_work_event', 
        name="change_work_event"),
    url(r"^change-unplanned-work-event/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_unplanned_work_event', 
        name="change_unplanned_work_event"),
    url(r"^sessions/$", 'valuenetwork.valueaccounting.views.sessions', name="sessions"),
    url(r"^change-event-date/$", 'valuenetwork.valueaccounting.views.change_event_date', name="change_event_date"),
    url(r"^change-event-qty/$", 'valuenetwork.valueaccounting.views.change_event_qty', name="change_event_qty"),
    url(r"^add-todo/$", 'valuenetwork.valueaccounting.views.add_todo', name="add_todo"),
    url(r"^todo-time/$", 'valuenetwork.valueaccounting.views.todo_time', name="todo_time"),
    url(r"^todo-description/$", 'valuenetwork.valueaccounting.views.todo_description', name="todo_description"),
    url(r"^todo-done/(?P<todo_id>\d+)/$", 'valuenetwork.valueaccounting.views.todo_done', name="todo_done"),
    url(r"^todo-decline/(?P<todo_id>\d+)/$", 'valuenetwork.valueaccounting.views.todo_decline', name="todo_decline"),
    url(r"^todo-mine/(?P<todo_id>\d+)/$", 'valuenetwork.valueaccounting.views.todo_mine', name="todo_mine"),
    url(r"^todo-change/(?P<todo_id>\d+)/$", 'valuenetwork.valueaccounting.views.todo_change', name="todo_change"),
    url(r"^todo-delete/(?P<todo_id>\d+)/$", 'valuenetwork.valueaccounting.views.todo_delete', name="todo_delete"),
    url(r"^labnotes-history/$", 'valuenetwork.valueaccounting.views.labnotes_history', name="labnotes_history"),
    url(r"^todo-history/$", 'valuenetwork.valueaccounting.views.todo_history', name="todo_history"),
    url(r"^open-todos/$", 'valuenetwork.valueaccounting.views.open_todos', name="open_todos"),
    url(r"^today/$", 'valuenetwork.valueaccounting.views.today', name="today"),
    url(r"^create-user-agent/$", 'valuenetwork.valueaccounting.views.create_user_and_agent', name="create_user_and_agent"),
    url(r"^delete-event/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_event', 
        name="delete_event"),
    url(r"^delete-citation-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_citation_event', 
        name="delete_citation_event"),
    url(r"^change-event/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_event', 
        name="change_event"),
    url(r"^test-patterns/$", 'valuenetwork.valueaccounting.views.test_patterns', 
        name="test_patterns"),
    url(r"^maintain-patterns/$", 'valuenetwork.valueaccounting.views.maintain_patterns', 
        name="maintain_patterns"),
    url(r"^maintain-patterns/(?P<use_case_id>\d+)/$", 'valuenetwork.valueaccounting.views.maintain_patterns', 
        name="maintain_patterns"),
    url(r"^change-pattern/(?P<pattern_id>\d+)/(?P<use_case_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_pattern', 
        name="change_pattern"),
    url(r"^add-pattern-use-case/(?P<use_case_id>\d+)/$", 'valuenetwork.valueaccounting.views.add_pattern_to_use_case', 
        name="add_pattern_to_use_case"),
    url(r"^remove-pattern-from-use-case/(?P<use_case_id>\d+)/(?P<pattern_id>\d+)/$", 'valuenetwork.valueaccounting.views.remove_pattern_from_use_case', 
        name="remove_pattern_from_use_case"),
    url(r"^resource-facets/$", 'valuenetwork.valueaccounting.views.resource_facet_table', 
        name="resource_facet_table"),
    url(r"^change-resource-facet-value/$", 'valuenetwork.valueaccounting.views.change_resource_facet_value', 
        name="change_resource_facet_value"),
    url(r"^exchange/(?P<exchange_id>\d+)/$", 'valuenetwork.valueaccounting.views.exchange_logging', name="exchange_logging"), 
    url(r"^create-exchange/(?P<use_case_identifier>\w+)/$", 'valuenetwork.valueaccounting.views.create_exchange', name="create_exchange"),
    url(r"^create-sale/$", 'valuenetwork.valueaccounting.views.create_sale', name="create_sale"),
    url(r"^create-distribution/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_distribution', name="create_distribution"),
    url(r"^json-context-agent-suppliers/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_context_agent_suppliers', name="json_context_agent_suppliers"),      
    url(r"^json-context-agent-customers/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_context_agent_customers', name="json_context_agent_customers"),      
    url(r"^json-customer-orders/(?P<customer_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_customer_orders', name="json_customer_orders"),      
    url(r"^json-order-customer/(?P<order_id>\d+)/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.json_order_customer', name="json_order_customer"),      
    url(r"^exchanges/$", 'valuenetwork.valueaccounting.views.exchanges', name="exchanges"), 
    url(r"^material-contributions/$", 'valuenetwork.valueaccounting.views.material_contributions', name="material_contributions"), 
    url(r"^sales-and-distributions/$", 'valuenetwork.valueaccounting.views.sales_and_distributions', name="sales_and_distributions"),  
    url(r"^sales-and-distributions/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.sales_and_distributions', name="sales_and_distributions"),  
    url(r'^add-unplanned-payment/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_unplanned_payment', 
        name="add_unplanned_payment"),  
    url(r"^change-unplanned-payment-event/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_unplanned_payment_event', 
        name="change_unplanned_payment_event"),
    url(r'^add-expense/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_expense', 
        name="add_expense"),  
    url(r"^change-expense-event/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_expense_event', 
        name="change_expense_event"),
    url(r'^add-unordered-receipt/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_unordered_receipt', 
        name="add_unordered_receipt"), 
    url(r'^add-receipt-to-resource/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_receipt_to_resource', 
        name="add_receipt_to_resource"),
    url(r'^add-contribution-to-resource/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_contribution_to_resource', 
        name="add_contribution_to_resource"),
    url(r"^change-receipt-event/(?P<event_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_receipt_event', 
        name="change_receipt_event"),
    url(r'^add-work-for-exchange/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_work_for_exchange', 
        name="add_work_for_exchange"),  
    url(r'^add-cash-contribution/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_cash_contribution', 
        name="add_cash_contribution"),  
    url(r'^add-cash-resource-contribution/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_cash_resource_contribution', 
        name="add_cash_resource_contribution"),  
    url(r'^add-material-contribution/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_material_contribution', 
        name="add_material_contribution"), 
    url(r'^add-unordered-receipt/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_unordered_receipt', 
        name="add_unordered_receipt"),
    url(r'^add-shipment/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_shipment', 
        name="add_shipment"),  
    url(r'^change-shipment-event/(?P<event_id>\d+)/$', 'valuenetwork.valueaccounting.views.change_shipment_event', 
        name="change_shipment_event"), 
    url(r'^add-cash-receipt/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_cash_receipt', 
        name="add_cash_receipt"), 
    url(r'^add-cash-receipt-resource/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_cash_receipt_resource', 
        name="add_cash_receipt_resource"), 
    url(r'^change-cash-receipt-event/(?P<event_id>\d+)/$', 'valuenetwork.valueaccounting.views.change_cash_receipt_event', 
        name="change_cash_receipt_event"), 
    url(r'^add-distribution/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.add_distribution', 
        name="add_distribution"), 
    url(r'^change-distribution-event/(?P<event_id>\d+)/$', 'valuenetwork.valueaccounting.views.change_distribution_event', 
        name="change_distribution_event"), 
    url(r'^change-exchange-work-event/(?P<event_id>\d+)/$', 'valuenetwork.valueaccounting.views.change_exchange_work_event', 
        name="change_exchange_work_event"), 
    url(r"^create-supplier/$", 'valuenetwork.valueaccounting.views.create_supplier', 
        name="create_supplier"),
    url(r'^delete-exchange/(?P<exchange_id>\d+)/$', 'valuenetwork.valueaccounting.views.delete_exchange', 
        name="delete_exchange"),
    url(r"^explore/$", 'valuenetwork.valueaccounting.views.explore', name="explore"),
    url(r"^unfold-commitment/(?P<commitment_id>\d+)/$", 'valuenetwork.valueaccounting.views.unfold_commitment', name="unfold_commitment"),
    url(r"^unfold-process/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.unfold_process', name="unfold_process"),
    url(r"^misc/$", 'valuenetwork.valueaccounting.views.misc', name="misc"),
    url(r"^cleanup/$", 'valuenetwork.valueaccounting.views.cleanup', name="cleanup"),
    url(r"^cleanup-processes/$", 'valuenetwork.valueaccounting.views.cleanup_processes', name="cleanup_processes"),
    url(r"^cleanup-old-processes/$", 'valuenetwork.valueaccounting.views.cleanup_old_processes', name="cleanup_old_processes"),
    url(r"^cleanup-resourcetypes/$", 'valuenetwork.valueaccounting.views.cleanup_resourcetypes', name="cleanup_resourcetypes"),
    url(r"^cleanup-resources/$", 'valuenetwork.valueaccounting.views.cleanup_resources', name="cleanup_resources"),
    url(r'^exchange-events-csv/$', 'valuenetwork.valueaccounting.views.exchange_events_csv', 
        name="exchange_events_csv"),
    url(r"^locations/$", 'valuenetwork.valueaccounting.views.locations', name="locations"),
    url(r"^create-location/$", 'valuenetwork.valueaccounting.views.create_location', name="create_location"),
    url(r"^change-location/(?P<location_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_location', name="change_location"),
    url(r"^agent/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.agent', name="agent"),
    url(r"^accounting/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.accounting', name="accounting"),
    url(r"^change-agent/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_agent', name="change_agent"),
    url(r"^create-user/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_user', name="create_user"),
    url(r"^agent-associations/(?P<agent_id>\d+)/$", 'valuenetwork.valueaccounting.views.agent_associations', 
        name="agent_associations"),
    url(r"^change-commitment-quantities/(?P<order_item_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_commitment_quantities', 
        name="change_commitment_quantities"),
    url(r"^change-workflow-project/(?P<order_item_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_workflow_project', 
        name="change_workflow_project"),        
    url(r"^add-order-item/(?P<order_id>\d+)/$", 'valuenetwork.valueaccounting.views.add_order_item', 
        name="add_order_item"),
    url(r"^change-process-plan/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_process_plan', 
        name="change_process_plan"),
    url(r"^delete-workflow-process/(?P<order_item_id>\d+)/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_workflow_process', 
        name="delete_workflow_process"),
    url(r"^create-process-for-streaming/(?P<order_item_id>\d+)/$", 'valuenetwork.valueaccounting.views.create_process_for_streaming', 
        name="create_process_for_streaming"),
    url(r"^insert-process-for-streaming/(?P<order_item_id>\d+)/(?P<process_id>\d+)/$", 'valuenetwork.valueaccounting.views.insert_process_for_streaming', 
        name="insert_process_for_streaming"),
    url(r"^closed-work-orders/$", 'valuenetwork.valueaccounting.views.closed_work_orders', name="closed_work_orders"),  
    url(r"^resource-type-lists/$", 'valuenetwork.valueaccounting.views.resource_type_lists', name="resource_type_lists"),
    url(r"^create-resource-type-list/$", 'valuenetwork.valueaccounting.views.create_resource_type_list', name="create_resource_type_list"),
    url(r"^change-resource-type-list/(?P<list_id>\d+)/$", 'valuenetwork.valueaccounting.views.change_resource_type_list', name="change_resource_type_list"),
    url(r"^delete-resource-type-list/(?P<list_id>\d+)/$", 'valuenetwork.valueaccounting.views.delete_resource_type_list', name="delete_resource_type_list"),
)

