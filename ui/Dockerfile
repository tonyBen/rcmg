FROM node:16 as builder
WORKDIR /cloud
COPY . ./
RUN rm -rf /cloud/dist
RUN pwd
RUN ls -l
RUN npm run build:prod
#RUN ls -l 
#RUN mkdir -p /usr/share/nginx/html/
#RUN cd ./dist
#RUN ls -l
#COPY * /usr/share/nginx/html/
#RUN ls -l /usr/share/nginx/html/
#ADD /cloud/dist/* /usr/share/nginx/html/
#ADD /usr/share/nginx/html/ /cloud/dist/*

FROM nginx:latest
COPY --from=builder /cloud/dist/* /usr/share/nginx/html/
COPY --from=builder /cloud/dist/static /usr/share/nginx/html/static

RUN ls /usr/share/nginx/html/
CMD ["nginx","-g","daemon off;"]
#CMD ["npm","run","dev"]
