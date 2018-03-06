#!/usr/bin/env python

import cgitb
import requests
import collections
import urllib
import httplib2
cgitb.enable()

def open_ticket():
    import cgi
    from src_script.MySQL import Database
    form = cgi.FieldStorage()
    db = Database(host='localhost', username='root', password='', db='alarm_ticket')
    query_detail="""SELECT * FROM tts WHERE cat_id = '{0}'""".format(form["cat_id"].value)
    lst_detail = db.query(query_detail)[0]

    print '<h2> open ticket </h2>'
    print '<form class ="form-horizontal" action="/cgi-enabled/checkvalue.py" method="post" name="ticket_form"  target = "_blank">'
    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="interaction"> interaction ID(Ticket) </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" readonly = "" class ="form-control" id="interaction" name="interaction">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="customertype" > Customer Type </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="customertype" name="customertype">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="status" > Status </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" readonly = "" class ="form-control" id="status" name="status" value="open">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients" > Recipients </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" readonly = "" class ="form-control" id="recipients" name="recipients" value="catma">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="incidentid" > Incident ID </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" readonly = "" class ="form-control" id="incident" name="incident">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="informant" > Informant </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="informant" name="informant" value="catma">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="catid" > CAT ID * </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="catid" name="catid" value="{0}">'.format(lst_detail['cat_id'])
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="email" > E-mail </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="email" name="email" value="catma@ait.co.th" >'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="source" > Name * </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="source" name="source" value="{0}">'.format(lst_detail['oss_source'])
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients "> category </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="recipients " name="recipients">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="source" > Destination</label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="destination" name="destination" value="{0}">'.format(lst_detail['oss_destination'])
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients "> Phone number </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="phonenumber" name="phonenumber" value="021041761">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="source" > Address </label>'
    print '<div class ="col-sm-4" >'
    print '<textarea type = "text" class ="form-control" id="address" name="address" rows="5" >{0}</textarea>'.format(lst_detail['address'])
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients ">SMS</label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="sms" name="sms">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="bandwidth"> Project Name </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="projectname" name="projectname">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients " > area </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="recipients " name="recipients">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="bandwidth"> Bandwidth </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="bandwidth" name="bandwidth">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients " > subarea </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="recipients " name="recipients" >'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="bandwidth"> Partners Name </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="partnername" name="partnername">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients " > Impact* </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="impact " name="impact" >'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="bandwidth"> Carrier Name </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="bandwidth" name="bandwidth">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients " > Urgency* </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="urgency " name="urgency">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="bandwidth"> Carrier Ticket </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="bandwidth" name="bandwidth">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients " > subarea </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="recipients " name="recipients" >'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="bandwidth"> Affected Service* </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="affectedservice" name="affectedservice">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="bandwidth"> Affected Cl* </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="affected_cl" name="affected_cl">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients "> Urgency </label>'
    print '<div class ="col-sm-4">'
    print '<input type = "text" class ="form-control" id="recipients" name="recipients">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="faulttime" > Fault Time * </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="faulttime" name="faulttime">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients " > Owner Group </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="recipients " name="recipients" value="{0}">'.format(lst_detail['owner_group'])
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="faulttime" > Up Time * </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" readonly="" id="uptime" name="uptime">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="recipients " > Assignment Group </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="assignment " name="assignment">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="faulttime" > Total Down Time </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" readonly="" id="totaltime" name="totaltime">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="faulttime" > EndToEnd Group </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="EndToEnd_group" name="EndToEnd_group">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="faulttime" > SLA Target Date </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" readonly="" id="sla_target_date" name="sla_target_date">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="faulttime" > Repair Team </label>'
    print '<div class ="col-sm-4" >'
    print '<input type = "text" class ="form-control" id="repair_team" name="repair_team">'
    print '</div>'
    print '</div>'

    print '<div class ="form-group">'
    print '<label class ="control-label col-sm-2" for ="title" > Title * </label>'
    print '<div class ="col-sm-10">'
    print '<input type = "text" class ="form-control" id="title" name="title">'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="title" > Description * </label>'
    print '<div class ="col-sm-2"></div>'
    print '<div class ="col-sm-10">'
    print '<textarea type = "text" class ="form-control" id="description" name="description"></textarea>'
    print '</div>'
    print '<label class ="control-label col-sm-2" for ="title" > comment </label>'
    print '<div class ="col-sm-2"></div>'
    print '<div class ="col-sm-10">'
    print '<textarea type = "text" class ="form-control" id="comment" name="comment"></textarea>'
    print '</div>'
    print '</div>'
    print '<button type="submit">save</button>'
    print '</form>'

def post_method():
    data = collections.OrderedDict()
    data['interaction'] =''
    data['customertype'] =''
    data['status'] =''
    data['recipients'] =''
    data['incident'] =''
    data['informant'] =''
    data['catid'] =''
    data['email'] =''
    data['source'] =''
    data['recipients'] =''
    data['destination'] =''
    data['phonenumber'] =''
    data['address ']=''
    data['sms ']=''
    data['projectname'] =''
    data['recipients'] =''
    data['bandwidth'] =''
    data['recipients'] =''
    data['partnername ']=''
    data['impact'] =''
    data['bandwidth'] =''
    data['urgency ']=''
    data['affectedservice'] =''
    data['affected_cl']=''
    data['faulttime'] =''
    data['uptime ']=''
    data['assignment'] =''
    data['totaltime ']=''
    data['EndToEnd_group'] =''
    data['sla_target_date ']=''
    data['repair_team'] =''
    data['title'] =''
    data['description'] =''
    data['comment'] =''
    r = requests.post("http://192.168.133.132/cgi-enabled/checkvalue.py?",data)
    # print r.


if __name__ == "__main__":
    from src_script.template import template_AT
    t = template_AT()
    t.print_header()
    t.print_menu()

    open_ticket()
    #post_method()
    t.print_close()
