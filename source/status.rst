:html_theme.sidebar_secondary.remove:
:sd_hide_title:

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Electrolize&family=Zen+Dots&display=swap');

        .bd-article-container {
            overflow-x: unset !important;
        }

        /* Add styles for status text */
        .status-container p.sd-card-text {
            font-weight: 600;
            margin: 0;
            padding: 0.5rem 1rem;
        }

    


        .sd-summary-title span {
            margin-right: 7px;
        }

        /* Custom tooltip styles */
        .sd-badge[data-tooltip] {
            position: relative;
            cursor: help;
            z-index: 3;
        }

        .sd-badge[data-tooltip]:hover::after {
            content: attr(data-tooltip);
            z-index:6;
            position: absolute;
            bottom: calc(100% + 8px);
            left: 50%;
            transform: translateX(-50%);
            padding: 8px 12px;
            background-color: var(--pst-color-surface);
            color: var(--pst-color-text-base);
            border: 1px solid var(--pst-color-border);
            border-radius: 4px;
            font-size: 12px;
            white-space: normal;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            font-family: var(--pst-font-family-base);
            font-weight: normal;
            width: max-content;
            max-width: 300px;
            text-align: center;
            pointer-events: none;
        }

        .sd-badge[data-tooltip]:hover::before {
            content: '';
            position: absolute;
            bottom: calc(100% + 4px);
            left: 50%;
            transform: translateX(-50%);
            border-width: 4px;
            border-style: solid;
            border-color: var(--pst-color-border) transparent transparent transparent;
            pointer-events: none;
        }

        .sd-badge[title] {
            text-decoration: none;
        }

        .electrolize {
            font-family: "Electrolize", sans-serif;
            font-weight: 1000;
            font-style: normal;
        }

        .zen-dots {
            font-family: "Zen Dots", sans-serif;
            font-style: normal;
        }

        /* Loading spinner */
        #loader {
            width: 120px;
            height: 120px;
            display: inline-block;
            position: relative;
        }
        #loader::after,
        #loader::before {
            content: '';  
            box-sizing: border-box;
            width:120px;
            height: 120px;
            border-radius: 50%;
            background: #FFF;
            position: absolute;
            left: 0;
            top: 0;
            animation: animloader 2s linear infinite;
        }
        #loader::after {
            animation-delay: 1s;
        }
        
        @keyframes animloader {
            0% {
                transform: scale(0);
                opacity: 1;
            }
            100% {
                transform: scale(1);
                opacity: 0;
            }
        }
        

        #deployments {
            display: flex;
            flex-direction: row;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
        }

        .nn-deployment {
            flex: 1 1 280px;
            border-radius: .5rem;
            max-width: 280px;
        }

        html[data-theme="dark"] .nn-deployment {
            border: 1px solid grey;
        }

        .nn-deployment:hover {
            z-index: 3;
        }

        .nn-card-body {
            display: flex;
            flex-direction: column;
            border-radius: .5rem;
            justify-content: space-between;
        }

        .nn-badges {
            
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            gap: 6px;
        }

        .nn-badges .sd-badge{
            
            white-space: wrap;
        }

        .nn-repo-id {
            font-size: 1rem;
            margin-bottom: 0.5rem;
            margin-right: 0.5rem;
        }

        .nn-copy-button {
            position: absolute !important;
            right: 2.3%;
            top: 4%
        }

        .nn-copy-button button {
            z-index: 4;
            opacity: 1;
            top: 0 !important;
            right: 0 !important;
           

        }

        .nn-snippet{
            display: none;
            position: absolute;
            bottom: 100%; /* Position above the icon */
            left: 0;       /* Align left edge of box with icon */
            border: 2px solid var(--pst-color-link-hover);
        }

        .nn-copy-button:hover .nn-snippet{
            display: block;
        }

      
    </style>


    <script>

        let ndif_url = "http://localhost:5001"
       

        function formatTimeRemaining(endTime) {
            const now = new Date();
            const end = new Date(endTime);
            
            const diff = end - now;
            
            if (diff < 0) return "Ended";
            
            const hours = Math.floor(diff / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            return `${hours}h ${minutes}m remaining`;
        }

        function update(message, cls) {
            document.querySelectorAll('div.sd-card-body.status-container').forEach(el => {
                el.classList.remove(...Array.from(el.classList).filter(cls => cls.startsWith('sd-bg')));
                el.classList.add(`sd-bg-${cls}`);
                el.classList.add(`sd-bg-text-${cls}`);
                el.querySelectorAll('div.sd-card-title').forEach(el => {
                    el.textContent = message;
                   
                });
            });
        }

        function loading(flag) {
            document.getElementById("loader").style.display = flag ? "block" : "none";
        }

        function getCalendarLink(calendar_id) {
            return `<a href="https://calendar.google.com/calendar/embed?src=${encodeURIComponent(calendar_id)}" target="_blank" class="sd-sphinx-override sd-btn sd-text-wrap"><span>View Dedicated Deployment Calendar ↗</span></a>`;
        }

        function getHuggingFaceLink(repo_id) {
            return `<a href="http://huggingface.co/${repo_id}" target="_blank" class="sd-stretched-link sd-hide-link-text"><span>HuggingFace Model Repository ↗</span></a>`;
        }

        function getConfigJson(configJsonString) {

            if (configJsonString === undefined || configJsonString === null) {
                return "";
            }

            let jsonObject = JSON.parse(configJsonString);
            let prettyPrintedJson = JSON.stringify(jsonObject, null, 4);
            prettyPrintedJson = prettyPrintedJson.replace(/"([^"]+)":/g, '"<b>$1</b>":');  
            return `<pre>${prettyPrintedJson}</pre>`;
        }

        function getBadge(content, sdcls, bg=true, tooltip=undefined, cls=undefined) {
            tooltip = tooltip ? `data-tooltip="${tooltip}"` : "";
            cls = cls ? cls : "";
            return `<span class="sd-sphinx-override sd-badge sd-${bg ? "bg" : "outline"}-${sdcls} sd-${bg ? "bg-" : ""}text-${sdcls} ${cls}" ${tooltip}>${content}</span>`
        }

        function getDeploymentLevelBadge(deployment_level){

            let tooltip = undefined;
            let color = undefined;
            let text = deployment_level

            switch(deployment_level) {
                case "HOT":
                    tooltip = "This model is on GPU and ready to serve.";
                    color = "success";
                    text = `<i class="fa-solid fa-microchip"></i>  Hot`
                    break;
                case "WARM":
                    tooltip = "This model is cached on CPU and will be quickly loaded into GPU when requested assuming it can be accomodated.";
                    color = "warning";
                    text = `<i class="fa-solid fa-fire"></i>  Warm`
                    break;
                case "COLD":
                    tooltip = "This model is downloaded and will be slowly loaded into GPU when requested assuming it can be accomodated.";
                    color = "primary";
                    text = `<i class="fa-regular fa-snowflake"></i>  Cold`
                    break;
            }
            
            return getBadge(text, color, bg=true, tooltip=tooltip, cls="electrolize")
        }

        function getApplicationStateBadge(application_state){

            if (application_state === undefined || application_state === null) {
                return "";
            }

            let color = undefined;
            let text = undefined;

            switch(application_state) {
                case "NOT_STARTED":
                    color = "warning";
                    text = `<i class="fa-solid fa-gear fa-spin"></i>  Not Started`
                    break;
                case "DEPLOYING":
                    color = "warning";
                    text = `<i class="fa-solid fa-gear fa-spin"></i>  Deploying`
                    break;
                case "DEPLOY_FAILED":
                    color = "danger";
                    text = `<i class="fa-solid fa-xmark"></i>  Deploy Failed`
                    break;
                case "RUNNING":
                    color = "success";
                    text = `<i class="fa-solid fa-check"></i>  Running`
                    break;
                case "UNHEALTHY":
                    color = "danger";
                    text = `<i class="fa-solid fa-xmark"></i>  Unhealthy`
                    break;
            }
            
            return getBadge(text, color, bg=true, tooltip=undefined, cls="electrolize")  
        }
        
        function getScheduleBadges(schedule) {

            if (schedule === undefined || schedule === null) {
                return "";
            }

            let now = new Date();
            let start = undefined;
            let end = undefined;

            if (schedule.start_time) {
                start = new Date(schedule.start_time);
            }
            if (schedule.end_time) {
                end = new Date(schedule.end_time);
            }
            
            if (!end || now > end) return "";

            if (start && now < start) {
                const startStr = start.toLocaleString(undefined, {
                    timeZoneName: 'short',
                    hour: 'numeric',
                    minute: 'numeric',
                    hour12: true
                });
                const duration = Math.round((end - start) / (1000 * 60 * 60));
                let text = `Starts ${startStr} (${duration}h duration)`
                let tooltip = "This model is scheduled to be deployed at a future time."
                let info_badge = getBadge(text, "muted", bg=false)
                let scheduled_badge = getBadge(`<i class="fa-solid fa-clock"></i>  Scheduled`, "info", bg=true, tooltip=tooltip, cls="electrolize")
                return `${info_badge} ${scheduled_badge}`
            }
            else {

                let text = formatTimeRemaining(schedule.end_time);
                let tooltip = "This model wont be evicted for the specified duration."
                let info_badge = getBadge(text, "muted", bg=false)
                let scheduled_badge = getBadge(`<i class="fa-solid fa-thumbtack"></i>  Pinned`, "info", bg=true, tooltip=tooltip, cls="electrolize")

                return `${info_badge} ${scheduled_badge}`
            }

        }

        function getModelClassBadge(class_name) {

            if (class_name === undefined || class_name === null) {
                return "";
            }

            let text = undefined;
            let color = "secondary"

            switch(class_name) {
                case "nnsight.modeling.language.LanguageModel":
                    text = `<i class="fa-solid fa-language"></i>  Language`
                    break;
               
            }

            return getBadge(text, color, bg=true, tooltip=undefined, cls="electrolize")
        }

        let codecell_id = 0;

        function getCopyButton(class_name, repo_id) {

            if (class_name === undefined || class_name === null) {
                return "";
            }

            let parts = class_name.split('.');
            let import_path = parts.slice(0, -1).join('.');
            let obj_name = parts[parts.length - 1];

            let code = `
 <span class="kn">from</span> <span class="nn">${import_path}</span> <span class="kn">import</span> <span class="n">${obj_name}</span>
                
 <span class="n">model</span> <span class="o">=</span> <span class="n">${obj_name}</span><span class="p">(</span><span class="s1">"${repo_id}"</span><span class="p">)</span>
                
 <span class="k">with</span> <span class="n">model</span><span class="o">.</span><span class="n">trace</span><span class="p">(</span><span class="s2">"The Eiffel Tower is in the city of"</span><span class="p">,</span> <span class="n">remote</span><span class="o">=</span><span class="s1">True</span><span class="p">)</span><span class="p">:</span>
                
    <span class="n">output</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">output</span><span class="o">.</span><span class="n">save</span><span class="p">()</span>`                

            let copy_button =  `
                <div class="nn-snippet">
                    <div class="highlight">
                        <pre tabindex="0" id="codecell${codecell_id}">
                            ${code}
                        </pre>
                    </div>
                </div>
                <div class="highlight">
                    <button class="copybtn o-tooltip--left" data-clipboard-target="#codecell${codecell_id}">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <title>Copy to clipboard</title>
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                            <rect x="8" y="8" width="12" height="12" rx="2"></rect>
                            <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2"></path>
                        </svg>
                    </button>
                </div>
                `

            codecell_id++;

            return copy_button;
        }

        document.addEventListener('DOMContentLoaded', function() {
            loading(true);

            update("Fetching NDIF status...", 'info');

            fetch(ndif_url + "/ping")
                .then((response) => {
                    if (response.status == 200) {
                        update("NDIF is up. Fetching model status...", 'info');

                        console.log('Ping success');
                        fetch(ndif_url + "/status")
                            .then((statsResponse) => {
                                loading(false);

                                if (statsResponse.status == 200) {
                                    statsResponse.json().then((response) => {
                                        console.log('Parsed response:', response);
                                        
                                        let infoString = '';
                                        let index = 0;

                                        if (!response.deployments || Object.keys(response.deployments).length === 0) {
                                            update("NDIF is up but there are no models deployed. Seems unintentional.", 'warning');
                                            return;
                                        }

                                        update("NDIF is operational.", 'success');

                                      
                                        // Sort deployments by deployment_level in the desired order
                                        const deploymentOrder = ["DEDICATED", "HOT", "WARM", "SCHEDULED", "COLD"];
                                        Object.entries(response.deployments)
                                            .sort(([, a], [, b]) => {
                                                const aLevel = deploymentOrder.indexOf(a.deployment_level);
                                                const bLevel = deploymentOrder.indexOf(b.deployment_level);
                                                // If same level, sort by schedule existence
                                                if (aLevel === bLevel) {
                                                    return (b.schedule ? 1 : 0) - (a.schedule ? 1 : 0);
                                                }
                                                // If not found, put at the end
                                                return (aLevel === -1 ? deploymentOrder.length : aLevel) - (bLevel === -1 ? deploymentOrder.length : bLevel);
                                            })
                                            .forEach(([key, deployment]) => {
                                            //const minutesleft = value.minutesleft;

                                            let class_name = deployment.model_key ? deployment.model_key.split(":")[0] : undefined;

                                            infoString += `
                                            <div class="nn-deployment sd-card sd-sphinx-override sd-shadow-sm sd-card-hover" data-repo-id="${deployment.repo_id}" data-deployment-level="${deployment.deployment_level}" data-application-state="${deployment.application_state}" data-schedule="${deployment.schedule}">
                                                <div class="sd-card-body nn-card-body">
                                                    <div class="nn-copy-button">
                                                        ${getCopyButton(class_name, deployment.repo_id)}
                                                    </div>
                                                    <div class="nn-repo-id electrolize">${deployment.repo_id}</div>
                                                    <div class="nn-badges">
                                                        ${getScheduleBadges(deployment.schedule)}
                                                        ${getModelClassBadge(class_name)}
                                                        ${getDeploymentLevelBadge(deployment.deployment_level)}
                                                        ${getApplicationStateBadge(deployment.application_state)}
                                                    </div>
                                                    
                                                </div>
                                                ${getHuggingFaceLink(deployment.repo_id)}
                                            </div>
                                            `
                                        });

                                        
                                        var status_hook = document.getElementById("status_hook");


                                        status_hook.innerHTML = `
                                            <div id="deployments">
                                                ${infoString}
                                            </div>
                                        `

                                        var status_info = document.querySelector('.status-info');
                                        var child = document.createElement('p');
                                        child.innerHTML = getCalendarLink(response.calendar_id);
                                        status_info.appendChild(child);
                                    
                                        // Start the schedule update timer
                                        //startScheduleTimer();

                                        console.log('Stats success');
                                    }).catch((jsonError) => {
                                        console.log('JSON parsing error:', jsonError);
                                    });
                                } else {
                                    update("Unable to get NDIF status.", 'danger');
                                }
                            })
                            .catch((statsError) => {
                                update("Unable to get NDIF status.", 'danger');
                                loading(false);

                                console.log('Stats error', statsError);
                            });
                    } else {
                        update("NDIF is unavailable", 'danger');
                        loading(false);
                        console.log('Ping error');
                    }
                })
                .catch((pingError) => {
                    update("NDIF is unavailable", 'danger');
                    loading(false);
                    console.error('Ping fetch failed:', pingError);
                });
        }, false);
    </script>


Status
======

.. card:: Getting Status
    :class-body: status-container
    :shadow: none
    :text-align: center

    

.. card::
    :shadow: none
    :class-body: status-info
    
    NNsight can be used to run local models without requiring a key. However, running experiments on NDIF remote models requires a free API key. To obtain a key, register for an `NDIF account <https://login.ndif.us>`_ which allows you to manage and generate keys.
    For information on API key configuration and remote system limits, please refer to our `Remote Execution Tutorial <https://nnsight.net/notebooks/features/remote_execution/>`_.

    Below, models are shown in various states of deployment, and their deployment level is shown in the leftmost badge (hover for more information on their meaning). Models not displayed here are in the lowest state of deployment, which means they are not even downloaded. 
    Upon request they may be able to be downloaded assuming there is space to accommodate and they don't require non-Hugging Face code and are not gated. 
    If there is a model that you believe should be accessible, please message the team on Discord or email.

    We currently have engineers on call Monday to Friday from 9 AM to 5 PM ET to assist with any connectivity issues for our remote models. Please reach out to us on `Discord <https://discord.com/invite/6uFJmCSwW7>`_ or via email at `info@ndif.us <mailto:info@ndif.us>`_.

.. raw:: html

    <div style="
        width:100%;
        display: flex;
        justify-content: center;
        ">
        <div id="loader"></div>
    </div>
    


    <div id="status_hook">
    </div>