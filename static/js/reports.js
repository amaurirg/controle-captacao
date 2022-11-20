function renderiza_relatorio_candidatos(url) {
    fetch(url, {
        method: 'get',
    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        const context = document.getElementById('chartCandidatos');
        new Chart(context, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Candidatos',
                    data: data.data,
                    backgroundColor: '#1678C2',
                    borderColor: '#FFF',
                    borderWidth: 0.2
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: true,
                        text: 'Relatório de Candidatos',
                        font: {
                            size: 20
                        },
                        padding: {
                            bottom: 30
                        }
                    }
                },
                layout: {
                    padding: {
                        top: 10,
                        bottom: 10,
                        left: 10,
                        right: 10
                    },
                },

            }
        })
    })
}

function renderiza_relatorio_inscritos(url) {
    fetch(url, {
        method: 'get',
    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        const context = document.getElementById('chartInscritos');
        new Chart(context, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Candidatos',
                    data: data.data,
                    backgroundColor: '#1678C2',
                    borderColor: '#FFF',
                    borderWidth: 0.2
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: true,
                        text: 'Relatório de Inscritos',
                        font: {
                            size: 20
                        },
                        padding: {
                            bottom: 30
                        }
                    }
                },
                layout: {
                    padding: {
                        top: 10,
                        bottom: 10,
                        left: 10,
                        right: 10
                    },
                },

            }
        })
    })
}

function renderiza_relatorio_alunos(url) {
    fetch(url, {
        method: 'get',
    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        const context = document.getElementById('chartAlunos');
        new Chart(context, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Candidatos',
                    data: data.data,
                    backgroundColor: '#1678C2',
                    borderColor: '#FFF',
                    borderWidth: 0.2
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: true,
                        text: 'Relatório de Alunos',
                        font: {
                            size: 20
                        },
                        padding: {
                            bottom: 30
                        }
                    }
                },
                layout: {
                    padding: {
                        top: 10,
                        bottom: 10,
                        left: 10,
                        right: 10
                    },
                },

            }
        })
    })
}

function renderiza_relatorio_exalunos(url) {
    fetch(url, {
        method: 'get',
    }).then(function (result) {
        return result.json()
    }).then(function (data) {
        const context = document.getElementById('chartExAlunos');
        new Chart(context, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Candidatos',
                    data: data.data,
                    backgroundColor: '#1678C2',
                    borderColor: '#FFF',
                    borderWidth: 0.2
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: true,
                        text: 'Relatório de Ex Alunos',
                        font: {
                            size: 20
                        },
                        padding: {
                            bottom: 30
                        }
                    }
                },
                layout: {
                    padding: {
                        top: 10,
                        bottom: 10,
                        left: 10,
                        right: 10
                    },
                },

            }
        })
    })
}